import yfinance as yf
import pandas as pd

def load_data(tickers, start="2020-01-01", end="2024-01-01"):
    data = yf.download(tickers, start=start, end=end, group_by="ticker")

    prices = pd.DataFrame()

    for ticker in tickers:
        try:
            prices[ticker] = data[ticker]["Adj Close"]
        except:
            prices[ticker] = data[ticker]["Close"]

    return prices.dropna(axis=1)