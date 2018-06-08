'''
### 1.
'''
import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Plot a linear regression between 'weight' and 'hp'
sns.lmplot(x='weight', y='hp', data=auto)

# Display the plot
plt.show()

'''
### 2.
'''
# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
'''### import numpy'''
import numpy as np

# Generate a green residual plot of the regression between 'hp' and 'mpg'
sns.residplot(x='hp', y='mpg', data=auto, color='green')

# Display the plot
plt.show()

'''
### 3.
'''

# Generate a scatter plot of 'weight' and 'mpg' using red circles
plt.scatter(auto['weight'], auto['mpg'], label='data', color='red', marker='o')

# Plot in blue a linear regression of order 1 between 'weight' and 'mpg'
'''
### label vs marker
### marker could be 'o', or 'x'
'''
sns.regplot(x='weight', y='mpg', data=auto, scatter=None, order = 1, color='blue', label='order 1')

# Plot in green a linear regression of order 2 between 'weight' and 'mpg'
sns.regplot(x='weight', y='mpg', data=auto, scatter=None, order = 2, color='green', label='order 2')

# Add a legend and display the plot
plt.legend(loc='upper right')
plt.show()

'''
### 4.
'''
# Plot a linear regression between 'weight' and 'hp', with a hue of 'origin' and palette of 'Set1'

'''### data = auto,
In the automobile dataset - which has been pre-loaded here as auto
'''
sns.lmplot(x='weight', y='hp', data = auto, hue='origin',palette='Set1')

# Display the plot
plt.show()

'''
### 5.
'''
# Plot linear regressions between 'weight' and 'hp' grouped row-wise by 'origin'
'''###Use the keyword argument row to group observations with the categorical column 'origin' in subplots organized in rows.'''

sns.lmplot(x='weight', y='hp', data = auto, row ='origin')

# Display the plot
plt.show()

'''
### 6.
'''
# Make a strip plot of 'hp' grouped by 'cyl'
''' ### In the first row of subplots, make a strip plot showing distribution of 'hp' values grouped horizontally by 'cyl' '''
plt.subplot(2,1,1)
sns.stripplot(x = 'cyl', y= 'hp', data = auto)

# Make the strip plot again using jitter and a smaller point size
plt.subplot(2,1,2)
sns.stripplot(x = 'cyl', y= 'hp', data = auto, jitter = True, size = 3)

# Display the plot
plt.show()

'''
### 7.
'''
# Generate a swarm plot of 'hp' grouped horizontally by 'cyl'
plt.subplot(2,1,1)
sns.swarmplot(x='cyl', y='hp', data=auto)

# Generate a swarm plot of 'hp' grouped vertically by 'cyl' with a hue of 'origin'
'''### with horizontal orientation (i.e., grouped vertically by 'cyl' with 'hp' value spread out horizontally)'''
plt.subplot(2,1,2)
sns.swarmplot(x='hp', y='cyl', data=auto, hue = 'origin',orient='h')

# Display the plot
plt.show()

'''
### 8.
'''
# Generate a violin plot of 'hp' grouped horizontally by 'cyl'
plt.subplot(2,1,1)
sns.violinplot(x='cyl', y='hp', data=auto)

# Generate the same violin plot again with a color of 'lightgray' and without inner annotations
plt.subplot(2,1,2)
sns.violinplot(x='cyl', y='hp', data=auto,inner=None, color = 'lightgray')

# Overlay a strip plot on the violin plot
sns.stripplot(x='cyl', y='hp', data=auto, size=1.5,jitter=True)

# Display the plot
plt.show()

'''
### 9.
'''
# Generate a joint plot of 'hp' and 'mpg'
sns.jointplot(x='hp', y='mpg', data=auto)

# Display the plot
plt.show()f

'''
### 10.
'''
# Print the first 5 rows of the DataFrame
print(auto.head())

# Plot the pairwise joint distributions from the DataFrame
sns.pairplot(auto)

# Display the plot
plt.show()

'''
### 11.
'''
# Print the first 5 rows of the DataFrame
print(auto.head())

# Plot the pairwise joint distributions grouped by 'origin' along with regression lines
'''### 'origin' is one of the hue '''
sns.pairplot(auto, kind = 'reg',hue = 'origin')

# Display the plot
plt.show()

'''
### 12.
'''
# Print the covariance matrix
print(cov_matrix)

# Visualize the covariance matrix using a heatmap
sns.heatmap(cov_matrix)

# Display the heatmap
plt.show()
