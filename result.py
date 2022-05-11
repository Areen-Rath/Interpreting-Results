import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('final.csv')

name = df["Name"].tolist()
mass = df["Mass"].tolist()
radii = df["Radius"].tolist()
distance = df["Distance"].tolist()
gravity = df["Gravity"].tolist()

plt.figure()
sns.barplot(x = name, y = mass)
plt.title("Name vs Mass")
plt.xlabel("Name")
plt.ylabel("Mass")
plt.show()

plt.figure()
sns.barplot(x = name, y = radii)
plt.title("Name vs Radius")
plt.xlabel("Name")
plt.ylabel("Radius")
plt.show()

plt.figure()
sns.barplot(x = name, y = distance)
plt.title("Name vs Distance")
plt.xlabel("Name")
plt.ylabel("Distance")
plt.show()

plt.figure()
sns.barplot(x = name, y = gravity)
plt.title("Name vs Gravity")
plt.xlabel("Name")
plt.ylabel("Gravity")
plt.show()