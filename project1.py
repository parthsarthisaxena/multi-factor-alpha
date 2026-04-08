import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Get data
stocks = [
    "RELIANCE.NS","TCS.NS","INFY.NS","HDFCBANK.NS","ICICIBANK.NS",
    "SBIN.NS","LT.NS","AXISBANK.NS","ITC.NS","HINDUNILVR.NS"
]

raw = yf.download(stocks, start="2020-01-01", end="2024-01-01")

# Handle column format
if "Adj Close" in raw.columns:
    data = raw["Adj Close"]
else:
    data = raw["Close"]

# Step 2: Factors
momentum = data.pct_change(20)
volatility = data.pct_change().rolling(20).std()

# Step 3: Z-score normalization
def zscore(df):
    return (df - df.mean()) / df.std()

momentum_z = zscore(momentum)
vol_z = zscore(-volatility)

# Step 4: Alpha (momentum focused)
alpha_score =  momentum_z 

# Volatility filter
alpha_score = alpha_score.where(volatility < volatility.quantile(0.9), 0)

# Trend filter (soft)
trend = data > data.rolling(50, min_periods=20).mean()
alpha_score = alpha_score.where(trend, alpha_score * 0.5)

# 🔥 IMPORTANT: remove invalid rows
valid_idx = alpha_score.dropna(how="all").index
data = data.loc[valid_idx]
alpha_score = alpha_score.loc[valid_idx]
volatility = volatility.loc[valid_idx]

# Step 5: Portfolio construction
weights = alpha_score.rank(axis=1, ascending=False)

portfolio = (weights <= 2).astype(int)

# Normalize weights
row_sum = portfolio.sum(axis=1)
portfolio = portfolio.div(row_sum.replace(0, np.nan), axis=0).fillna(0)

# Weekly rebalancing
rebalance_portfolio = portfolio.resample('ME').first()

portfolio = rebalance_portfolio.reindex(data.index).ffill().fillna(0)

# Step 6: Returns
returns = data.pct_change().loc[portfolio.index]

turnover = portfolio.diff().abs().sum(axis=1).fillna(0)
cost = 0.001  # transaction cost

strategy_returns = (portfolio.shift(1) * returns).sum(axis=1) - cost * turnover
strategy_returns = strategy_returns.replace([np.inf, -np.inf], np.nan).dropna()

cumulative_returns = (1 + strategy_returns).cumprod()

# Step 7: Plot
cumulative_returns.plot(label="Strategy")

benchmark = data.mean(axis=1).pct_change()
benchmark_cum = (1 + benchmark).cumprod()

benchmark_cum.plot(label="Benchmark")

plt.title("Strategy vs Benchmark")
plt.legend()
plt.savefig("comparison.png")
print("Comparison saved as comparison.png")

# Step 8: Metrics
if strategy_returns.std() != 0:
    sharpe = strategy_returns.mean() / strategy_returns.std() * (252**0.5)
else:
    sharpe = 0

max_drawdown = (cumulative_returns / cumulative_returns.cummax() - 1).min()

print("Sharpe:", sharpe)
print("Max Drawdown:", max_drawdown)
total_return = cumulative_returns.iloc[-1] - 1
print("Total Return (ROI):", total_return)
years = (cumulative_returns.index[-1] - cumulative_returns.index[0]).days / 365

cagr = (cumulative_returns.iloc[-1]) ** (1/years) - 1
print("CAGR:", cagr)