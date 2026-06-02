import pandas as pd
import os

folder = "data/raw"

for file in os.listdir(folder):

    if file.endswith(".csv"):

        path = os.path.join(folder, file)

        df = pd.read_csv(path)

        print("\n====================")
        print(file)
        print("====================")

        print("Rows:", len(df))
        print("Columns:", len(df.columns))

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicates:", df.duplicated().sum())