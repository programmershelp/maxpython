import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('planets.csv')

df.info()

df.describe()

df.columns

#Planet with Maximum Mass
print(df.iloc[df["Mass (10^24kg)"].idxmax()].Planet)
#Planet with maximum Density
print(df.iloc[df["Density (kg/m^3)"].idxmax()].Planet)
#Planet with maximum Surface Gravity
print(df.iloc[df["Surface Gravity(m/s^2)"].idxmax()].Planet)
#Planet with maximum Escape Velocity (km/s)
print(df.iloc[df["Escape Velocity (km/s)"].idxmax()].Planet)
#Planet with maximum moons
print(df.iloc[df["Number of Moons"].idxmax()].Planet)
#Planet with longest Length of Day (hours)
print(df.iloc[df["Length of Day (hours)"].idxmax()].Planet)

plt.figure(figsize=(15,9))
plt.style.use("dark_background")
sns.barplot(x = df['Planet'], y = df['Diameter (km)'])
plt.ylabel('Diameter (km)')
plt.xlabel('Planet')
plt.title('Planets Diameter')
plt.show()

plt.figure(figsize=(15,8))
plt.style.use("dark_background")
sns.barplot(x = df['Planet'], y = df['Density (kg/m^3)'])
plt.ylabel('Density (kg/m^3)')
plt.xlabel('Planet')
plt.title('Planets Density')
plt.show()

plt.figure(figsize=(15,8))
plt.style.use("dark_background")
sns.barplot(x = df['Planet'], y = df['Surface Gravity(m/s^2)'])
plt.ylabel('Surface Gravity in (m/s^2)')
plt.xlabel('Planet')
plt.title('Planets Surface Gravity')
plt.show()

plt.figure(figsize=(15,8))
plt.style.use("dark_background")
sns.barplot(x = df['Planet'], y = df['Number of Moons'])
plt.ylabel('Number of Moons')
plt.xlabel('Planet')
plt.title('Planets Number of Moons')
plt.show()

plt.figure(figsize=(15,8))
plt.style.use("dark_background")
sns.barplot(x = df['Planet'], y = df['Mean Temperature (C)'])
plt.ylabel('Mean Temperature (C)')
plt.xlabel('Planet')
plt.title('Planets Mean Temperature (C)')
plt.show()

plt.figure(figsize=(15,8))
plt.style.use("dark_background")
sns.barplot(x = df['Planet'], y = df['Length of Day (hours)'])
plt.ylabel('Length of Day (hours)')
plt.xlabel('Planet')
plt.title('Planets Length of Day (hours)')
plt.show()