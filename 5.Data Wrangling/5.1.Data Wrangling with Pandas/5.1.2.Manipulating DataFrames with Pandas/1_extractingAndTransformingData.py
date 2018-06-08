'''
1.Indexing and column rearrangement
'''
# Import pandas
import pandas as pd
import numpy as np

# Read in filename and set the index: election
'''### so country will be the index column'''
election = pd.read_csv(filename, index_col='county')

'''### Create a separate dataframe with the columns ['winner', 'total', 'voters']: results'''
results = election[['winner', 'total', 'voters']]

# Print the output of results.head()
print(results.head())

'''
2.Slicing rows
'''
# Slice the row labels 'Perry' to 'Potter': p_counties
p_counties = election.loc['Perry':'Potter',:]

# Print the p_counties DataFrame
print(p_counties)

'''### Slice the row labels 'Potter' to 'Perry' in reverse order: p_counties_rev'''
p_counties_rev = election.loc['Potter':'Perry':-1,:]

# Print the p_counties_rev DataFrame
print(p_counties_rev)

'''
3.### Slicing columns
'''
# Slice the columns from the starting column to 'Obama': left_columns
left_columns = election.loc[:,:'Obama']

# Print the output of left_columns.head()
print(left_columns.head())

# Slice the columns from 'Obama' to 'winner': middle_columns
middle_columns = election.loc[:,'Obama':'winner']

# Print the output of middle_columns.head()
print(middle_columns.head())

# Slice the columns from 'Romney' to the end: 'right_columns'
right_columns = election.loc[:,'Romney':]

# Print the output of right_columns.head()
print(right_columns.head())

'''
4.Subselecting DataFrames with lists
'''
# Create the list of row labels: rows
rows = ['Philadelphia', 'Centre', 'Fulton']

# Create the list of column labels: cols
cols = ['winner', 'Obama', 'Romney']

# Create the new DataFrame: three_counties
'''### election.loc[...] !!! '''
three_counties = election.loc[rows,cols]

# Print the three_counties DataFrame
print(three_counties)

'''
5.Thresholding data
'''
# Create the boolean array: high_turnout
high_turnout = election['turnout'] > 70

# Filter the election DataFrame with the high_turnout array: high_turnout_df
high_turnout_df = election.loc[high_turnout]

# Print the high_turnout_results DataFrame
print(high_turnout_df)

'''
6.### Thresholding data
'''
# Create the boolean array: high_turnout
high_turnout = election['turnout'] > 70

'''### Filter the election DataFrame with the high_turnout array:''' high_turnout_df
high_turnout_df = election.loc[high_turnout]

# Print the high_turnout_results DataFrame
print(high_turnout_df)

'''
7.### Filtering columns using other columns
'''
# Import numpy
import numpy as np

# Create the boolean array: too_close
too_close = election['margin'] < 1

'''### Assign np.nan to the 'winner' column where the results were too close to call'''
election.loc[too_close, 'winner'] = np.nan

# Print the output of election.info()
print(election.info())

'''
8.### Filtering using NaNs
'''
# Select the 'age' and 'cabin' columns: df
df = titanic[['age','cabin']]

# Print the shape of df
print(df.shape)

# Drop rows in df with how='any' and print the shape
print(df.dropna(how='any').shape)

# Drop rows in df with how='all' and print the shape
print(df.dropna(how='all').shape)

# Call .dropna() with thresh=1000 and axis='columns' and print the output of .info() from titanic
print(titanic.dropna(thresh=1000, axis='columns').info())
