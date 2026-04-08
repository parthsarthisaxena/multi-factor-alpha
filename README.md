# 📈 Multi-Factor Alpha Strategy (Indian Equities)

## 🚀 Overview

A systematic multi-factor equity strategy designed to generate alpha using momentum signals and risk filters, tested on Indian equity markets.

This project builds a **data-driven portfolio** that aims to outperform a benchmark while maintaining controlled risk through quantitative techniques.

---

## 🧠 Strategy Logic

The model combines multiple quantitative signals:

### 📊 Factors Used

* **Momentum (Primary Signal)**
  Captures trend persistence using 20-day returns.

* **Volatility Filter**
  Reduces exposure to highly volatile stocks.

* **Trend Filter**
  Adjusts allocation based on whether stocks trade above their 50-day moving average.

---

## ⚙️ Portfolio Construction

* Rank stocks daily using a composite alpha score
* Select **top-performing stocks (top 2)**
* Equal-weight allocation
* Apply **monthly rebalancing**
* Normalize weights to maintain capital consistency

---

## 💰 Backtesting Features

* Transaction cost modeling (0.1% per trade)
* Turnover-based cost deduction
* Cumulative return tracking
* Benchmark comparison (equal-weight portfolio)

---

## 📊 Results

| Metric                 | Value |
| ---------------------- | ----- |
| **CAGR**               | ~24%  |
| **Sharpe Ratio**       | ~1.2  |
| **Max Drawdown**       | ~30%  |
| **Total Return (ROI)** | ~138% |

---

## 📉 Strategy vs Benchmark

![Strategy Performance](results/comparison.png)

---

## 🧪 Key Insights

* Momentum is the dominant driver of returns
* Monthly rebalancing improves stability and reduces noise
* Risk filters help control drawdowns
* Strategy demonstrates **positive alpha vs benchmark**

---

## ⚠️ Limitations

* Limited universe (10 stocks)
* No out-of-sample testing
* No sector constraints
* Limited factor set

---

## 🔮 Future Improvements

* Expand to **Nifty 50 universe**
* Add additional factors (value, quality, volume)
* Implement position sizing models
* Perform walk-forward validation
* Build a modular backtesting engine

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* yFinance

---

## 📌 Project Structure

```bash
multi-factor-alpha/
 ├── src/
 │    └── strategy.py
 ├── results/
 │    ├── comparison.png
 │    └── results.csv
 ├── README.md
 ├── requirements.txt
```

---

## ⚡ How to Run

```bash
pip install -r requirements.txt
python src/strategy.py
```

---

## 👨‍💻 Author

Parth Sarthi Saxena

---

## ⭐ Summary

This project demonstrates the application of **quantitative finance concepts**, including alpha generation, portfolio construction, and realistic backtesting with transaction costs.

It reflects a structured approach to building **systematic trading strategies** used in quantitative finance.
