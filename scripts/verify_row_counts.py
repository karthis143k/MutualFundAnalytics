import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

files = {
    "01_fund_master_cleaned.csv": "dim_fund",
    "02_nav_history_cleaned.csv": "fact_nav",
    "03_aum_by_fund_house_cleaned.csv": "fact_aum",
    "04_monthly_sip_inflows_cleaned.csv": "sip_inflows",
    "05_category_inflows_cleaned.csv": "category_inflows",
    "06_industry_folio_count_cleaned.csv": "industry_folio",
    "07_scheme_performance_cleaned.csv": "fact_performance",
    "08_investor_transactions_cleaned.csv": "fact_transactions",
    "09_portfolio_holdings_cleaned.csv": "portfolio_holdings",
    "10_benchmark_indices_cleaned.csv": "benchmark_indices"
}

for file, table in files.items():

    csv_rows = len(
        pd.read_csv(f"data/processed/{file}")
    )

    db_rows = pd.read_sql(
        f"SELECT COUNT(*) as cnt FROM {table}",
        engine
    ).iloc[0]["cnt"]

    print(
        f"{table}: CSV={csv_rows} | DB={db_rows}"
    )

print("\nRow Count Verification Complete")