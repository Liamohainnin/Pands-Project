import pandas
import matplotlib.pyplot as plt 
import seaborn as sns
import pylab


sns.set(style="ticks")
df = pandas.read_csv(r'C:\Users\User1\source\repos\pands-project\iris.csv',  #Read csv file into data frame
            #index_col='Index', 
           # parse_dates=['sepal_width'],
            header=0, 
            names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width','species'])
#print (df.head (5))
df.to_csv('Iris_modified.csv')

df.hist (figsize=(10, 10))                                                      # Plot all variables as Histograms
pylab.suptitle("Histograms of variables in Iris dataset", fontsize="xx-large")

plt.savefig('Histogramofallvariables.png')                                      # Save plots of all variables to png

VariableSummary=df.describe ()                                                  # Generate summary of all the variables in the Iris Dataset
print (df.describe ())
VariableSummary.to_csv('Summary.csv')                                           # Export summary of all the variables in the Iris Dataset to csv file


sns.pairplot(df, hue="species" , palette="husl")                                # Generate scatterplot of each pair of variables in the Iris Dataset
plt.show()
plt.savefig('Scatterplotofallvariables.png')                                    # Save scatterplot of each pair of variables to png


print (df.head (5))
print (df.groupby('species')["sepal_length",'sepal_width','petal_length', 'petal_width'].median())
print (df.groupby('species').agg ({"sepal_length":['mean', 'median','std'],'sepal_width':['mean', 'median','std'],'petal_length':['mean', 'median','std'], 'petal_width':'sum'}))

print (df.groupby('species').agg(sepal_length_Mean=('sepal_length', 'mean'), sepal_length_Median=('sepal_length', 'median'), sepal_length_Std=('sepal_length', 'std'),petal_length_Mean=('petal_length', 'mean'), petal_length_Median=('petal_length', 'median'), petal_length_Std=('petal_length', 'std'),sepal_width_Mean=('sepal_width', 'mean'), sepal_width_Median=('sepal_width', 'median'), sepal_width_Std=('sepal_width', 'std'),petal_width_Mean=('petal_width', 'mean'), petal_width_Median=('petal_width', 'median'), petal_width_Std=('petal_width', 'std')))
Summary = df.groupby('species').agg(sepal_length_Mean=('sepal_length', 'mean'), sepal_length_Median=('sepal_length', 'median'), sepal_length_Std=('sepal_length', 'std'),petal_length_Mean=('petal_length', 'mean'), petal_length_Median=('petal_length', 'median'), petal_length_Std=('petal_length', 'std'),sepal_width_Mean=('sepal_width', 'mean'), sepal_width_Median=('sepal_width', 'median'), sepal_width_Std=('sepal_width', 'std'),petal_width_Mean=('petal_width', 'mean'), petal_width_Median=('petal_width', 'median'), petal_width_Std=('petal_width', 'std'))
Summary.to_csv('Summary.csv')
sns.pairplot(Summary)
plt.show()
Summary.hist(hue="species")
plt.show()


plt.figure(figsize = (10, 7)) 
#x = Summary["sepal_length_Mean"] 
x1 = df.loc[df.species=='setosa', 'sepal_length']
x2 = df.loc[df.species=='versicolor', 'sepal_length']
x3 = df.loc[df.species=='virginica', 'sepal_length']

kwargs = dict(alpha=0.5, bins=20)
sns.pairplot(kwargs)
plt.show()
#plt.hist(x, bins = 20, color = "green") 
plt.hist(x1, **kwargs, color='g', label='setosa')
plt.hist(x2, **kwargs, color='b', label='versicolor')
plt.hist(x3, **kwargs, color='c', label='virginica')
plt.title("sepal_length") 
plt.xlabel("sepal_length") 
plt.ylabel("Count") 
plt.legend()
plt.savefig('sepal_length.png')
plt.show() 


