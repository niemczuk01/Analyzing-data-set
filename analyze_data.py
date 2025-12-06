import pandas as pd

def main():
    df = pd.read_csv("data/swimmers_times.csv")

    print("=== FIRST FIVE ROWS ===")
    print(df.head(), "\n")

    print("=== DATAFRAME INFO ===")
    print(df.info(), "\n")

    print("=== SUMMARY STATISTICS ===")
    print(df.describe(include='all'), "\n")

    #Indexing

    print("=== SINGLE ROW BY LABEL (loc) ===")
    print(df.loc[0], "\n")

    print("=== SINGLE ROW BY POSITION (iloc) ===")
    print(df.iloc[0], "\n")

    print("=== SLICE OF ROWS BY LABEL (0:3) ===")
    print(df.loc[0:3], "\n")

    print("=== SLICE OF ROWS BY POSITION (0:3) ===")
    print(df.iloc[0:3], "\n")

    print("=== SINGLE COLUMN: Event ===")
    print(df["Event"].head(), "\n")

    print("=== SINGLE CELL [0, 'Time'] ===")
    print(df.loc[0, "Time"], "\n")

    #Filter by speed and strok

    print("=== FILTER: TIMES FASTER THAN 52 SECONDS (numerical condition) ===")
    fast_filter = df[df["Time"].astype(str).str.replace(":", ".", regex=False).astype(float) < 52]
    print(fast_filter.head(), "\n")

    print("=== FILTER: COUNTRY = USA AND EVENT CONTAINS 'Freestyle' ===")
    both_filter = df[(df["Country"] == "USA") & (df["Event"].str.contains("Freestyle"))]
    print(both_filter.head(), "\n")

    #Dropping and adding columns

    print("=== ADDING COLUMN: Time_as_float (converted numeric time) ===")
    df["Time_as_float"] = df["Time"].astype(str).str.replace(":", ".", regex=False).astype(float)
    print(df.head(), "\n")

    print("=== DROPPING COLUMN: Time ===")
    df = df.drop(columns=["Time"])
    print("Remaining columns:", df.columns.tolist(), "\n")

    #Group by average time by country
    print("=== GROUPBY: Average Converted Time by Country ===")
    result = df.groupby("Country")["Time_as_float"].mean()
    print(result, "\n")


if __name__ == "__main__":
    main()

