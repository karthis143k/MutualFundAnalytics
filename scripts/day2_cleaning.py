import pandas as pd
import os

RAW_FOLDER = "data/raw"
PROCESSED_FOLDER = "data/processed"

os.makedirs(PROCESSED_FOLDER, exist_ok=True)

print("Day 2 Cleaning Started...")

# ==========================
# NAV HISTORY CLEANING
# ==========================

nav_df = pd.read_csv(
    f"{RAW_FOLDER}/02_nav_history.csv"
)

print(nav_df.head())

print(nav_df.columns)

# convert date column
nav_df["date"] = pd.to_datetime(
    nav_df["date"],
    errors="coerce"
)

# sort
nav_df = nav_df.sort_values(
    ["amfi_code", "date"]
)

# forward fill NAV
nav_df["nav"] = (
    nav_df.groupby("amfi_code")["nav"]
    .ffill()
)

# remove invalid NAV
nav_df = nav_df[
    nav_df["nav"] > 0
]

# remove duplicates
nav_df = nav_df.drop_duplicates()

# save cleaned file
nav_df.to_csv(
    f"{PROCESSED_FOLDER}/02_nav_history_cleaned.csv",
    index=False
)

print("NAV cleaned successfully")
# ==========================
# INVESTOR TRANSACTIONS
# ==========================

txn_df = pd.read_csv(
    f"{RAW_FOLDER}/08_investor_transactions.csv"
)

print("\nTransaction Columns:")
print(txn_df.columns)

print(txn_df.head())
# ==========================
# CLEAN INVESTOR TRANSACTIONS
# ==========================

txn_df["transaction_date"] = pd.to_datetime(
    txn_df["transaction_date"],
    errors="coerce"
)

txn_df["transaction_type"] = (
    txn_df["transaction_type"]
    .str.strip()
    .str.title()
)

allowed_txn = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

txn_df = txn_df[
    txn_df["transaction_type"].isin(allowed_txn)
]

txn_df = txn_df[
    txn_df["amount_inr"] > 0
]

print("\nKYC Status Values:")
print(txn_df["kyc_status"].unique())

txn_df = txn_df.drop_duplicates()

txn_df.to_csv(
    f"{PROCESSED_FOLDER}/08_investor_transactions_cleaned.csv",
    index=False
)

print("Investor Transactions Cleaned Successfully")
# ==========================
# SCHEME PERFORMANCE
# ==========================

perf_df = pd.read_csv(
    f"{RAW_FOLDER}/07_scheme_performance.csv"
)

print("\nPerformance Columns:")
print(perf_df.columns)

print(perf_df.head())
# ==========================
# CLEAN SCHEME PERFORMANCE
# ==========================

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in numeric_cols:
    perf_df[col] = pd.to_numeric(
        perf_df[col],
        errors="coerce"
    )

# Flag invalid expense ratios
invalid_expense = perf_df[
    (perf_df["expense_ratio_pct"] < 0.1) |
    (perf_df["expense_ratio_pct"] > 2.5)
]

print("\nInvalid Expense Ratio Records:")
print(len(invalid_expense))

# Keep only valid rows
perf_df = perf_df[
    (perf_df["expense_ratio_pct"] >= 0.1) &
    (perf_df["expense_ratio_pct"] <= 2.5)
]

perf_df = perf_df.drop_duplicates()

perf_df.to_csv(
    f"{PROCESSED_FOLDER}/07_scheme_performance_cleaned.csv",
    index=False
)

print("Scheme Performance Cleaned Successfully")
files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    df = pd.read_csv(f"{RAW_FOLDER}/{file}")
    df = df.drop_duplicates()

    output_name = file.replace(".csv", "_cleaned.csv")

    df.to_csv(
        f"{PROCESSED_FOLDER}/{output_name}",
        index=False
    )

print("All Remaining Files Cleaned")