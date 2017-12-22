 from pandas import DataFrame, read_csv

import matplotlib.pyplot as plt
import pandas as pd
import sys
import os
import matplotlib

names = ['Aaron', 'Amanda', 'Grace', 'Jeff', 'Josh', 'Kevin', 'Scott']
births = [94, 82, 94, 72, 93, 84, 85]

print('-----------------------')

BabyDataSet = list(zip(names,births));
print(BabyDataSet)
print('-----------------------')

df = pd.DataFrame(data = BabyDataSet, columns=['Names','Births'])
print(df)
print('-----------------------')

df.to_csv('births.csv',index=False,header=False)
Location = r'/Users/rditlaav/Documents/Python/Python_Tutorials/pandas/births.csv'
df = pd.read_csv(Location, names=['Names','Births'])

os.remove(Location)

print(df.dtypes)

print('-----------------------')
df = df.sort_values(['Births'], ascending=False)
print(df);

print('-----------------------')
df = df.sort_values(['Births'], ascending=True)
print(df)

print('-----------------------')
df['Births'].plot()
MaxValue = df['Births'].max()
MaxName = df['Names'][df['Births'] == df['Births'].max()].values
Text = str(MaxValue) + " - " + MaxName
plt.annotate(Text, xy=(1, MaxValue), xytext=(8,0), xycoords=('axes fraction', 'data'), textcoords='offset points')
print("The most popular name")
print(df[df['Births'] == df['Births'].max()])

print('-----------------------')

