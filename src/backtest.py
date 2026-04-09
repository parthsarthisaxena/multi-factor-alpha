import numpy as np
import matplotlib.pyplot as plt

def run_backtest(prices, weights, transaction_cost=0.001):
    returns = prices.pct_change().fillna(0)

    strategy_returns = (weights * returns).sum(axis=1)

    # Transaction cost
    turnover = weights.diff().abs().sum(axis=1)
    costs = turnover * transaction_cost

    strategy_returns = strategy_returns - costs

    cumulative_returns = (1 + strategy_returns).cumprod()

    # Metrics
    risk_free_rate = 0.06
    rf_daily = risk_free_rate / 252

    excess_returns = strategy_returns - rf_daily

    sharpe = 0
    if excess_returns.std() != 0:
        sharpe = (excess_returns.mean() / excess_returns.std()) * np.sqrt(252)

    drawdown = cumulative_returns / cumulative_returns.cummax() - 1
    max_drawdown = drawdown.min()

    years = len(cumulative_returns) / 252
    cagr = cumulative_returns.iloc[-1] ** (1 / years) - 1

    # Save plots
    plt.figure()
    cumulative_returns.plot(title="Equity Curve")
    plt.savefig("results/equity_curve.png")

    plt.figure()
    drawdown.plot(title="Drawdown")
    plt.savefig("results/drawdown.png")

    return {
        "Sharpe": sharpe,
        "CAGR": cagr,
        "Max Drawdown": max_drawdown
    }