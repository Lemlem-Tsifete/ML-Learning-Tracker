import pandas as pd

df_csv = pd.read_csv("iris.data.txt", delimiter=",")
print(df_csv.to_string())
print(df_csv.describe())

print(df_csv.isnull().sum())

df_csv.to_csv("cleaned_data.csv", index=False)
print("Cleaned data saved as cleaned_data.csv")