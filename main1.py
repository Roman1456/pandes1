import pandas as pd

df = pd.read_csv('Space_Corrected (1).csv')
df.info()

a = df['Status Rocket'].value_counts()
print(a)