import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')

mass = df["Mass"].tolist()
radii = df["Radius"].tolist()
gravity = df["Gravity"].tolist()

x = []
for index, radius in enumerate(radii):
    x.append([radius, mass[index]])

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = "k-means++", random_state = 42)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

plt.figure()
sns.lineplot(range(1, 11), wcss, marker = "o", color = "green")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

"""
    Conclusion: As seen in the figure, we can see that we can clearly notice 2 bends after which we see an
    almost straight line, therefore concluding we have 3 clusters.
"""