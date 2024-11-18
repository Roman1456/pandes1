import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Space_Corrected (1).csv')
df.info()
a = df['Status Mission'].value_counts()

b = df[df['Status Mission']== 'Success']
compayt = b['Company Name'].value_counts()
top = compayt.head(5)

top.plot(kind='bar',color='blue',figsize=(10,5))
plt.title("Топ-5 компанії з найбільшою кількістю успішніх запусків")
plt.xlabel("Компанія")
plt.ylabel("Кількість успішніх запусків")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()