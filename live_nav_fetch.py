import requests
import pandas as pd

funds = {
    "hdfc_top100": "125497",
    "sbi_bluechip": "119551",
    "icici_bluechip": "120503",
    "nippon_largecap": "118632",
    "axis_bluechip": "119092",
    "kotak_bluechip": "120841"
}

for fund_name, scheme_code in funds.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_path = f"data/raw/{fund_name}.csv"

        nav_df.to_csv(file_path, index=False)

        print(f"{fund_name} saved successfully")

    else:
        print(f"Failed to fetch {fund_name}")