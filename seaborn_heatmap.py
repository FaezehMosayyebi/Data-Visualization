"""Aim:

Testing the results of adding and multiplying two features in a Data Fram

"""

#Import

import pandas as pd               # For making DataFrame
import seaborn as sns             # For making heatmap
import matplotlib.pyplot as plt   # For making subplots

#Defining a dataframe

df = pd.DataFrame({'v1' : [1,1,1,2,2,2,3,3,3],                     # Data Frame
                   'v2' : [100,200,300,100,200,300,100,200,300]
                   })
df['v1 + v2'] = df['v1'] + df['v2']             #Adding two features
df['v1 * v2'] = df['v1'] * df['v2']             #multiplying two features
display(df)                                     #Displaying the result

#Generating heatmaps

#Preparing Data
df_add = df.pivot(index = 'v1', columns = 'v2', values = 'v1 + v2')
df_mult = df.pivot(index = 'v1', columns = 'v2', values = 'v1 * v2')

#Making subplots and give names to them
fig, ax = plt.subplots(2,1)         
ax[0].title.set_text('v1 + v2')
ax[1].title.set_text('v2 * v2')

#Generating heatmaps
sns.heatmap(df_add, ax = ax[0])
sns.heatmap(df_mult, ax = ax[1])

