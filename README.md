Mutual Fund Analytics Platform

Project Overview

The Mutual Fund Analytics Platform was developed as part of the Bluestock Data Analytics Internship Capstone Project. The project focuses on building an end-to-end analytics solution for mutual fund performance evaluation, investor behavior analysis, risk assessment, and business intelligence reporting.

The platform integrates data engineering, exploratory data analysis, financial performance analytics, advanced risk modeling, and interactive dashboard visualization using Python, SQLite, and Power BI.

Project Scale

* 10 Datasets
* 40 Mutual Fund Schemes
* 46,000+ NAV Records
* 32,778 Investor Transactions
* 4-Page Interactive Power BI Dashboard



Project Objectives

* Analyze mutual fund industry growth and AUM trends.
* Evaluate fund performance using financial metrics.
* Study investor behavior and SIP trends.
* Perform advanced risk analytics.
* Build an interactive Power BI dashboard.
* Generate actionable business insights.

Technologies Used

* Python
* Pandas
* NumPy
* SQLite
* SQLAlchemy
* Plotly
* Matplotlib
* Power BI
* Git
* GitHub

Data Sources

The project utilizes the following datasets:

* Fund Master
* NAV History
* AUM by Fund House
* Monthly SIP Inflows
* Category Inflows
* Industry Folio Count
* Scheme Performance
* Investor Transactions
* Portfolio Holdings
* Benchmark Indices

ETL Pipeline

Extract

* Collected data from multiple CSV datasets.

Transform

* Data cleaning and validation.
* Missing value handling.
* Duplicate removal.
* Feature engineering.
* Calculation of financial metrics.

Load

* Loaded cleaned datasets into SQLite.
* Created analytical tables for reporting and dashboarding.

Database Design

SQLite Star Schema:
Dimension Tables

* dim_fund
* dim_date

Fact Tables

* fact_nav
* fact_transactions
* fact_performance
* fact_aum

Exploratory Data Analysis

Performed analysis on:

* Investor Demographics
* SIP Trends
* AUM Growth
* Category Inflows
* Folio Growth
* Fund Category Distribution

Generated visualizations:

* SIP Trend Chart
* AUM Growth Chart
* Category Heatmap
* Folio Growth Chart
* Top Performing Funds Analysis

Performance Analytics

Calculated metrics:

* CAGR (1-Year, 3-Year, 5-Year)
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown
* Fund Scorecard

Key Finding:

* SBI Small Cap Fund achieved the highest overall Fund Score.
* ICICI Prudential Liquid Fund recorded the highest Sharpe Ratio (7.68).

Advanced Analytics

Implemented:

* Historical VaR (95%)
* Conditional VaR (CVaR)
* Rolling 90-Day Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* Fund Recommendation Engine
* Sector HHI Concentration Analysis

Key Finding:

* 1,332 investors were identified as At-Risk through SIP continuity analysis.

Dashboard Overview

Power BI Dashboard Pages:

1. Industry Overview
2. Fund Performance
3. Investor Analytics
4. SIP & Market Trends

Features:

* KPI Cards
* Interactive Filters
* Drill-through Navigation
* Dynamic Visualizations

Deliverables

* Final_Report.pdf
* Bluestock_MF_Presentation.pptx
* bluestock_mf_dashboard.pbix
* Dashboard.pdf
* Advanced_Analytics.ipynb
* var_cvar_report.csv
* rolling_sharpe_chart.png
* recommender.py
* run_pipeline.py

Project Structure

data/
reports/
notebooks/
scripts/
dashboard/

How to Run

```bash
python scripts/run_pipeline.py
```

Open Dashboard:

```text
bluestock_mf_dashboard.pbix
```

Conclusion

The Mutual Fund Analytics Platform successfully combines data engineering, financial analytics, risk modeling, and business intelligence into a unified solution. The project provides actionable insights for investors, analysts, and fund managers through advanced analytics and interactive dashboards.


Bonus Analytics
- Markowitz Efficient Frontier Portfolio Optimization
- Monte Carlo Simulation for 5-Year NAV Forecasting
- Optimal Portfolio Allocation Analysis
- Risk-Return Trade-off Evaluation
