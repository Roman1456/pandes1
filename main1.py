import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Space_Corrected (1).csv')
df.info()

a = df['Status Rocket'].value_counts()
a.plot(kind='pie',color=['green','red'])
plt.title("Кількість ракет за статусом")
plt.show()