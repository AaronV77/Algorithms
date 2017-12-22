import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

web_stats = { 'Day': [1,2,3,4,5,6],
              'Visitors': [32,65,44,75,102,22],
              'Bounce_Rate': [66,36,55,49,29,88]}

df = pd.DataFrame(web_stats)

print('\n', df.head())
print('\n', df.tail())
print('\n', df.tail(2))

print('\n',df.set_index('Day'))             # This will create an index / new dataframe.
print('\n',df.head())                       # So when we get down here it returns the basic dataframe.

df2 = df.set_index('Day')                   # When we do this it will create a new pandas dataframe.
print('\n',df2.head())                      # It then will allows us to print the head of the indexed dataframe.

df.set_index('Day', inplace=True)           # This will change the original dataframe to the indexed one because of inplace=True
print('\n', df.head())

print('\n', df['Visitors'])                       # Will just print the column of visitors.
print('\n', df.Visitors)                          # Same thing as above.

df = pd.DataFrame(web_stats)
print('\n', df[['Bounce_Rate', 'Visitors']])            # Will print two colums of data.
print('\n', df.Visitors.tolist())                         # Will convert the visitors column into a list.
print('\n', np.array(df[['Bounce_Rate', 'Visitors']]))    # Will convert it to a 2D array.

df3 = pd.DataFrame(np.array(df[['Bounce_Rate', 'Visitors']]))
print('\n', df3)
