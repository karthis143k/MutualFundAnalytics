import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def calculate_sharpe_ratio(returns, risk_free_rate=0.06):
    excess_returns = returns.mean() * 252 - risk_free_rate
    volatility = returns.std() * np.sqrt(252)

    if volatility == 0:
        return 0

    return excess_returns / volatility


def calculate_sortino_ratio(returns, risk_free_rate=0.06):
    downside_returns = returns[returns < 0]

    if len(downside_returns) == 0:
        return 0

    downside_std = downside_returns.std() * np.sqrt(252)

    excess_returns = returns.mean() * 252 - risk_free_rate

    return excess_returns / downside_std


def calculate_max_drawdown(nav_series):
    rolling_max = nav_series.cummax()

    drawdown = (
        nav_series - rolling_max
    ) / rolling_max

    return drawdown.min() * 100


def main():

    nav_path = BASE_DIR / "data" / "raw" / "02_nav_history.csv"

    nav = pd.read_csv(nav_path)

    nav["date"] = pd.to_datetime(nav["date"])

    nav = nav.sort_values(["amfi_code", "date"])

    nav["daily_return"] = (
        nav.groupby("amfi_code")["nav"]
        .pct_change()
    )

    sample_fund = nav[
        nav["amfi_code"] == nav["amfi_code"].iloc[0]
    ]

    returns = sample_fund["daily_return"].dropna()

    sharpe = calculate_sharpe_ratio(returns)

    sortino = calculate_sortino_ratio(returns)

    max_dd = calculate_max_drawdown(
        sample_fund["nav"]
    )

    print(f"Sharpe Ratio: {sharpe:.2f}")
    print(f"Sortino Ratio: {sortino:.2f}")
    print(f"Maximum Drawdown: {max_dd:.2f}%")


if __name__ == "__main__":
    main()