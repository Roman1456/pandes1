import pandas as pd

df = pd.read_csv('Space_Corrected (1).csv')
df.info()
df[" Rocket"] = pd.to_numeric(df[" Rocket"], errors='coerce')

df[" Rocket"].fillna(df[" Rocket"].mean(), inplace=True)
print("Порожні значення замінено на середні значення")

# Заміна коми на крапку в усіх значеннях DataFrame
df[" Rocket"] = df[" Rocket"].replace('.', ',', regex=True)


