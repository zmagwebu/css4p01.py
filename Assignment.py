# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 13:57:11 2024

@author: zmagwebu
"""

import pandas

file = pandas.read_csv("C:/Users/zmagwebu/CSS_2024_Assignment/movie_dataset.csv")

print(file)
print(file.info())
print(file.describe())

# import pandas as pd

# df = pd.read_csv("C:/Users/zmagwebu/CSS_2024_Assignment/movie_dataset.csv", index_col=0)
# ####

# df.dropna(subset=['Revenue (Millions)'], inplace = True)
# df.dropna(subset=['Metascore'], inplace = True)
# print(df.info())
# print(df.describe())

# import pandas as pd
# column_names = ['Title', 'Genre', 'Description', 'Director', 'Actors', 'Year', 'Runtime_(Minutes)',	'Rating', 'Votes',	'Revenue_(Millions)', 'Metascore']
# df = pd.read_csv("C:/Users/zmagwebu/CSS_2024_Assignment/movie_dataset.csv", header=None, names= column_names)
# print(column_names)


import pandas as pd
df = pd.read_csv("C:/Users/zmagwebu/CSS_2024_Assignment/movie_dataset.cleaned.csv")
print(file)
print(file.info())
print(file.describe())

pd.set_option('display.max_columns', 70)
mean_Title = df['Rating'].mean()
print(df)
df = df.sort_values(by = 'Rating', ascending = False)
print(df)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.barplot(x=avg_rating_by_genre.index, y=avg_rating_by_genre.values)
plt.title('Average Rating by Genre')
plt.xlabel('Genre')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)
plt.show()
print(df.describe())

highest_rated_movie = df[df['Rating'] == df['Rating'].max()]
print("Highest Rated Movie:")
print(highest_rated_movie)
import pandas as pd


print(df.columns)
import pandas as pd
average_revenue = df['Revenue_Millions'].mean()
print("Non-numeric values or missing values found in the 'Revenue_Millions' column. Handling the