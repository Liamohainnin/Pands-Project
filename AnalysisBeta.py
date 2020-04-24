import pandas
import matplotlib.pyplot as plt 
import seaborn as sns
sns.set(style="ticks")
df = pandas.read_csv(r'C:\Users\User1\source\repos\pands-project\iris.csv', 
            #index_col='Index', 
           # parse_dates=['sepal_width'],
            header=0, 
            names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width','species'])
df.head (5)
df.to_csv('Iris_modified.csv')
print (df.head (25))
print (df.describe ())
#from pandas.plotting import scatter_matrix
#scatter_matrix(df)
sns.pairplot(df, hue="species")
plt.show()
df.hist(hue="species")
plt.show()
#
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


