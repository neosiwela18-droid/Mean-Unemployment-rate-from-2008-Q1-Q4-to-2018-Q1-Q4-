import pandas as pd
import statistics as ss
import matplotlib.pyplot as plt

city = []
rates = []
df = pd.read_csv("C:\\Users\\acer\\Desktop\\Coding\\Python\\data projects\\unemployment\\South Africa_AdministrativeArea1.csv")

man = df.groupby('placeName')

for i, m in man:
    rates.append(ss.mean(m["UnemploymentRate"]))
    city.append(i)

x = city
y = rates

plt.barh(x, y)
plt.xlabel("Mean Unemployment rate(%)", fontweight = "bold", labelpad= 20)
plt.ylabel("Provinces", fontweight = "bold", labelpad=20)
plt.title("Mean Unemployment rate from 2008(Q1-Q4) to 2018(Q1-Q4)", fontweight="bold")
plt.margins(x=0.1, y=0.1)  
plt.grid(axis="x", alpha = 0.3)
plt.show()
