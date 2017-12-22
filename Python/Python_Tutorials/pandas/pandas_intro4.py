import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import sys 
import matplotlib

names = ['Aaron', 'Amanda', 'Grace', 'Jeff', 'Josh', 'Kevin', 'Scott']

print('------------------')
random.seed(500);
random_names = [names[random.randint(low=0,high=len(names))] for i in range(1000)]
print(random_names[:10])

print('------------------')
births = [random.randint(low=0,high=1000) for i in range(1000)]
print(births[:10])

print('------------------')
BabyDataSet = list(zip(random_names,births))
print(BabyDataSet[:10])

df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
df['Names'].unique()

print('------------------')
name = df.groupby('Names')
df = name.sum()
print(df)

print('------------------')
df['Births'].plot.bar()
print("The most popular name")
print(df.sort_values(by="Births", ascending=False))
print('------------------')
