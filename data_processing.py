import pandas as pd
import os

data_folder = "data"

files = [
    "daily_sales_data_0.csv",
    "daily_sales_data_1.csv",
    "daily_sales_data_2.csv"
]

dfs = []

for file in files:
    path = os.path.join(data_folder, file)
    df = pd.read_csv(path)

    df = df[df["product"] == "pink morsel"]

    df["price"] = df["price"].replace(r'[\$,]', '', regex=True).astype(float)

    df["sales"] = df["quantity"] * df["price"]

    df = df[["sales", "date", "region"]]

    dfs.append(df)

final_df = pd.concat(dfs)

final_df.to_csv("formatted_sales.csv", index=False)

print("Processing complete")
