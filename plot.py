import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')

mass = df["Mass"].tolist()
radii = df["Radius"].tolist()
gravity = df["Gravity"].tolist()

mass.sort()
radii.sort()
gravity.sort()

plt.plot()
sns.scatterplot(x = radii, y = mass)
plt.title("Stars 1")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()

plt.plot()
sns.scatterplot(x = mass, y = gravity)
plt.title("Stars 2")
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.show()