import pandas as pd

def zscore(df):
    return (df - df.mean()) / df.std()

def compute_returns(prices):
    return prices.pct_change().fillna(0)