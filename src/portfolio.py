import pandas as pd

def construct_portfolio(alpha):
    weights = pd.DataFrame(index=alpha.index, columns=alpha.columns)

    prev_w = pd.Series(0.0, index=alpha.columns)

    for date in alpha.index:
        # 🔥 Monthly rebalance
        if date.day != 1:
            weights.loc[date] = prev_w
            continue

        scores = alpha.loc[date].dropna()

        if len(scores) < 10:
            weights.loc[date] = prev_w
            continue

        # 🔥 ONLY strongest signals
        longs = scores.nlargest(5)
        #shorts = scores.nsmallest(5)

        w = pd.Series(0.0, index=scores.index)

        # 🔥 Equal weights (IMPORTANT)
        w.loc[longs.index] = 1 / 5
        #w.loc[shorts.index] = -1 / 5
        w = w.reindex(alpha.columns).fillna(0)
        prev_w = w
        weights.loc[date] = w

    return weights.fillna(0)