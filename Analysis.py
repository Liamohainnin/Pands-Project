#   Liam O Hainnin
#   Program for analysis and representation of the Fischers Iris dataset
#   Completed as part of project for Programming and Scripting module 2020
#   It carries out following operations
#   Read csv file into data frame
#   Plots all variables as Histograms
#   Saves plots of all variables to png
#   Generates summary of all the variables in the Iris Dataset
#   Exports summary of all the variables in the Iris Dataset to csv file
#   Generates scatterplot of each pair of variables in the Iris Dataset
#   Saves scatterplot of each pair of variables to png
#   Plot horizontal bar chart with sub plots to allow viewing of the stats grouped by species to be viewed side by side
#   Hides legend to avoid covering of bars

import pandas
import matplotlib.pyplot as plt 
import seaborn as sns
import pylab



sns.set(style="ticks")
df = pandas.read_csv(r'C:\Users\User1\source\repos\pands-project\iris.csv',     # Read csv file into data frame

            header=0, 
            names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width','species'])
#print (df.head (5))
df.to_csv('Iris_modified.csv')

# Plot all variables as Histograms
df.hist (figsize=(10, 10))                                                      
pylab.suptitle("Histograms of variables in Iris dataset", fontsize="xx-large")

# Save plots of all variables to png
plt.savefig('Histogramofallvariables.png')                                      

# Generate summary of all the variables in the Iris Dataset
VariableSummary=df.describe ()                                                 
print (df.describe ())

# Export summary of all the variables in the Iris Dataset to csv file
VariableSummary.to_csv('Summary.csv')                                         

# Generate scatterplot of each pair of variables in the Iris Dataset
sns.pairplot(df, hue="species" , palette="husl")                                
plt.show()

# Save scatterplot of each pair of variables to png
plt.savefig('Scatterplotofallvariables.png')                                    

print (df.groupby('species').agg(sepal_length_Mean=('sepal_length', 'mean'), sepal_length_Median=('sepal_length', 'median'), sepal_length_Std=('sepal_length', 'std'),petal_length_Mean=('petal_length', 'mean'), petal_length_Median=('petal_length', 'median'), petal_length_Std=('petal_length', 'std'),sepal_width_Mean=('sepal_width', 'mean'), sepal_width_Median=('sepal_width', 'median'), sepal_width_Std=('sepal_width', 'std'),petal_width_Mean=('petal_width', 'mean'), petal_width_Median=('petal_width', 'median'), petal_width_Std=('petal_width', 'std')))
Summary = df.groupby('species').agg(sepal_length_Mean=('sepal_length', 'mean'), sepal_length_Median=('sepal_length', 'median'), sepal_length_Std=('sepal_length', 'std'),petal_length_Mean=('petal_length', 'mean'), petal_length_Median=('petal_length', 'median'), petal_length_Std=('petal_length', 'std'),sepal_width_Mean=('sepal_width', 'mean'), sepal_width_Median=('sepal_width', 'median'), sepal_width_Std=('sepal_width', 'std'),petal_width_Mean=('petal_width', 'mean'), petal_width_Median=('petal_width', 'median'), petal_width_Std=('petal_width', 'std'))
Summary.to_csv('SummarybySpecies.csv')

# Plot horizontal bar chart with sub plots to allow viewing of the stats grouped by species to be viewed side by side
# Hiding legend to avoid covering of bars
Summary.plot.barh(subplots=True,legend= False,fontsize=10, figsize=(16, 16), align='center')
# Adjust sublot positioning to allow easy viewing of the data increase hspace on subplots to avoid titles overlapping plots
plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9, hspace=0.5)

plt.show()

plt.savefig('AggregatedDataStatsGroupedBySpeciesHorBarChart.png')  





