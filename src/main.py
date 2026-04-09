from data_loader import load_data
from factors import compute_factors
from portfolio import construct_portfolio
from backtest import run_backtest

import matplotlib.pyplot as plt

# 🔥 Nifty universe
tickers = [
"RELIANCE.NS","TCS.NS","INFY.NS","HDFCBANK.NS","ICICIBANK.NS",
"HINDUNILVR.NS","SBIN.NS","BHARTIARTL.NS","ITC.NS","LT.NS",
"KOTAKBANK.NS","AXISBANK.NS","ASIANPAINT.NS","MARUTI.NS",
"TITAN.NS","SUNPHARMA.NS","ULTRACEMCO.NS","NESTLEIND.NS",
"BAJFINANCE.NS","WIPRO.NS","NTPC.NS","POWERGRID.NS",
"JSWSTEEL.NS","TATASTEEL.NS","ONGC.NS","COALINDIA.NS",
"HCLTECH.NS","TECHM.NS","DRREDDY.NS","CIPLA.NS"
]

# Step 1: Load data
prices = load_data(tickers)

# Step 2: Compute factors
alpha = compute_factors(prices)

# 🔥 NO LOOKAHEAD
alpha = alpha.shift(1)

# 🔥 IC CALCULATION
future_returns = prices.pct_change().shift(-1)
ic = alpha.corrwith(future_returns, axis=1)

print("IC Mean:", ic.mean())

# 🔥 Rolling IC
rolling_ic = ic.rolling(60).mean()

plt.figure()
rolling_ic.plot(title="Rolling IC (60-day)")
plt.savefig("results/rolling_ic.png")

# 🔥 WALK-FORWARD SPLIT
split_date = "2022-01-01"

train_prices = prices[prices.index < split_date]
test_prices = prices[prices.index >= split_date]

alpha = compute_factors(prices).shift(1)
# TRAIN
alpha_train = alpha[alpha.index < split_date]
weights_train = construct_portfolio(alpha_train)
train_results = run_backtest(train_prices, weights_train)

# TEST (OUT OF SAMPLE)
alpha_test = alpha[alpha.index >= split_date]
weights_test = construct_portfolio(alpha_test)
test_results = run_backtest(test_prices, weights_test)

print("===== TRAIN PERFORMANCE =====")
for k, v in train_results.items():
    print(f"{k}: {v:.4f}")

print("===== TEST PERFORMANCE =====")
for k, v in test_results.items():
    print(f"{k}: {v:.4f}")