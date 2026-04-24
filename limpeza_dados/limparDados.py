import pandas as pd

df = pd.read_csv('limpeza_dados/data.csv', encoding='utf8', skipinitialspace=True)
df = df[]
df = df.columns.str.strip()
print(df.head())
