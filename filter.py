import pandas as pd

df = pd.read_csv('data.csv')

name = df["Name"].tolist()
distance = df["Distance"].tolist()
mass = df["Mass"].tolist()
radii = df["Radius"].tolist()
gravity = df["Gravity"].tolist()

stars = []
for index, name in enumerate(name):
    stars.append([name, distance[index], mass[index], radii[index], gravity[index]])

distance_supporting_stars = []
for index, i in enumerate(distance):
    if i < 100:
        distance_supporting_stars.append(stars[index])

gravity_supporting_stars = []
for index, star in enumerate(distance_supporting_stars):
    if 150 < gravity[index] < 350:
        gravity_supporting_stars.append(df.iloc[index])

df.to_csv('final.csv')