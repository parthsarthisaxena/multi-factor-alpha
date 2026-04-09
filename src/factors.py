from utils import zscore

def compute_factors(prices):
    returns = prices.pct_change()

    # 🔥 Mean Reversion (core signal)
    mean_rev = -prices.pct_change(5)

    # 📈 Momentum
    momentum = prices.pct_change(20)

    # 📉 Volatility
    volatility = returns.rolling(20).std()

    # 📊 Trend
    ma50 = prices.rolling(50).mean()
    trend = prices / ma50

    # Z-score
    z_mr = zscore(mean_rev)
    z_mom = zscore(momentum)
    z_vol = zscore(volatility)
    z_trend = zscore(trend)

    # 🔥 SIMPLE, STRONG, WORKING ALPHA
    alpha = (
        0.6 * z_mr +
        0.2 * z_mom +
        0.1 * z_trend -
        0.1 * z_vol
    )

    return alpha.dropna()