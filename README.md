# Consumer Shopping Trends 2026 — End-to-End Data Analysis

## Project Overview
An end-to-end data analysis project on consumer shopping behaviour
using Excel, Python, SQL and Power BI.

**Dataset:** 11,789 rows · 25 features · 0 null values

---

## Tools Used
| Tool | Purpose |
|------|---------|
| Excel / Google Sheets | Data cleaning, pivot tables, charts |
| Python (pandas, seaborn) | EDA, feature engineering, visualisation |
| MySQL | Data querying, window functions |
| Power BI | Interactive dashboard |

---

## Project Structure
consumer-shopping-trends-2026/
├── data/
│   ├── Consumer_Shopping_Trends_2026.csv   # original dataset
│   └── cleaned_data.csv                    # cleaned + engineered
├── notebooks/
│   └── EDA_analysis.py                     # full Python EDA
├── sql/
│   └── shopping_analysis.sql               # 8 SQL queries
├── images/
│   ├── 01_shopping_preference.png
│   ├── 02_age_vs_preference.png
│   ├── 03_correlation_heatmap.png
│   ├── 04_income_vs_spend.png
│   ├── 05_digital_score_boxplot.png
│   ├── 06_spend_by_income_band.png
│   ├── dashboard_overview.png
│   ├── dashboard_demographics.png
│   ├── dashboard_behaviour.png
│   └── dashboard_city_analysis.png
├── powerbi/
│   └── consumer_shopping_dashboard.pbix
└── README.md
---

## Key Insights
- Tier 1 city customers spend **25% more** than Tier 3 customers
- Younger customers (18–25) have the **highest digital score**
- Store shoppers show **higher brand loyalty** than online shoppers
- High income customers prefer **online shopping** (62% online spend ratio)

---

## Feature Engineering
Five new columns created during analysis:
- `age_group` — 18-25, 26-35, 36-50, 51+
- `income_band` — Low, Medium, High
- `total_spend` — online + store spend combined
- `online_spend_ratio` — share of spend going online
- `digital_score` — composite tech + trust + internet score

---

## Dashboard Preview
![Overview](https://raw.githubusercontent.com/Sauravx4/consumer-shopping-trends-2026/main/images/Dashboard.png)

---

## How to Run
1. Clone this repo
2. Install requirements: `pip install pandas numpy matplotlib seaborn`
3. Run: `python notebooks/EDA_analysis.py`
4. Open `sql/shopping_analysis.sql` in MySQL Workbench
5. Open `powerbi/consumer_shopping_dashboard.pbix` in Power BI Desktop

---

## Connect with Me
- LinkedIn:https://www.linkedin.com/in/saurav-codease/
- Kaggle: https://www.kaggle.com/sauravmourya
