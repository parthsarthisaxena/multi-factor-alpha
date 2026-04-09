# 📈 Multi-Factor Alpha Strategy (Indian Equities)
Achieves ~24% CAGR with Sharpe ~1.2 using momentum-based alpha signals on Indian equities.

## 🚀 Overview

This project implements a **systematic multi-factor trading strategy** on Indian equities, combining mean reversion and momentum signals to generate alpha.

The strategy is designed with a **quantitative research workflow**, including factor modeling, portfolio construction, transaction cost modeling, and out-of-sample validation.

---

## 🧠 Strategy Logic

The model combines multiple factors:

* **Mean Reversion (Short-term)** – captures price reversals
* **Momentum (Medium-term)** – captures trend persistence
* **Trend Filter** – based on moving averages
* **Volatility Filter** – reduces exposure to risky assets

All factors are normalized using **z-scores** and combined into a composite alpha signal.

---

## ⚙️ Portfolio Construction

* Select **top 5 stocks** based on alpha signal
* Long-only allocation (equal weight)
* Monthly rebalancing to reduce turnover
* Transaction costs included (0.1% per trade)

---

## 📊 Performance (Out-of-Sample)

| Metric           | Value     |
| ---------------- | --------- |
| **Sharpe Ratio** | **0.76**  |
| **CAGR**         | **18.3%** |
| **Max Drawdown** | **-19%**  |

---

## 🔍 Validation & Research

* **Information Coefficient (IC): ~0.01**
* Walk-forward validation (train/test split)
* Rolling IC analysis for signal stability

---

## 📈 Key Insights

* Weak alpha signals (~IC 0.01) can still be profitable with proper portfolio construction
* Long-only structure outperforms long-short under realistic transaction costs
* Low turnover significantly improves net returns
* Simpler models can outperform over-engineered approaches

---

## ⚠️ Limitations

* Limited universe (Nifty 30 subset)
* No sector/beta neutrality applied in final version
* Performance sensitive to transaction costs and execution

---

## 🔮 Future Improvements

* Expand to full Nifty 50 universe
* Add sector and beta neutrality
* Incorporate additional factors (value, quality)
* Improve execution modeling (slippage, liquidity constraints)

---

## 🛠️ Tech Stack

* Python
* Pandas / NumPy
* Matplotlib
* yFinance

---

## 📂 Project Structure

```
multi-factor-alpha/
│
├── src/
│   ├── main.py
│   ├── data_loader.py
│   ├── factors.py
│   ├── portfolio.py
│   ├── backtest.py
│   └── utils.py
│
├── results/
│   ├── equity_curve.png
│   ├── drawdown.png
│   └── rolling_ic.png
│
├── README.md
├── requirements.txt
```

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python src/main.py
```

---

## 👨‍💻 Author

**Parth Sarthi Saxena**

---

## ⭐ Summary

This project demonstrates a **complete quant research pipeline**:

* Alpha generation
* Portfolio construction
* Backtesting with costs
* Signal validation

It reflects a practical approach to building **systematic trading strategies** used in quantitative finance.
