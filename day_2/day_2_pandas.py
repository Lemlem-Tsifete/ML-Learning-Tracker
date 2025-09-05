import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, None, 28],
    "Score": [85, 90, None, 70, 95]
}

df = pd.DataFrame(data)
print(df.to_string())

df_clean = df.dropna()
print(df_clean)

df_fill_mean = df.fillna(df.mean(numeric_only=True))
print(df_fill_mean)