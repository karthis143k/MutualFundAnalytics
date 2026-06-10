import pandas as pd

print("Starting recommender...")

funds = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print("Data loaded")

risk = input(
    "Enter Risk Appetite (Low/Moderate/High): "
)

result = funds[
    funds["risk_grade"]
    .str.contains(
        risk,
        case=False,
        na=False
    )
]

result = result.sort_values(
    "sharpe_ratio",
    ascending=False
)

print(
    result[
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio"
        ]
    ].head(3)
)
print(funds["risk_grade"].unique())