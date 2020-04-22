import pandas
df = pandas.read_csv(r'C:\Users\User1\source\repos\pands-project\iris.csv', 
            #index_col='Index', 
           # parse_dates=['sepal_width'],
            header=0, 
            names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width','species'])
df.head (5)
df.to_csv('Iris_modified.csv')
print (df.head (25))
print (df.describe ())

print (df.groupby('species')["sepal_length",'sepal_width','petal_length', 'petal_width'].median())
print (df.groupby('species').agg ({"sepal_length":['mean', 'median','std'],'sepal_width':['mean', 'median','std'],'petal_length':['mean', 'median','std'], 'petal_width':'sum'}))

print (df.groupby('species').agg(sepal_length_Mean=('sepal_length', 'mean'), sepal_length_Median=('sepal_length', 'median'), sepal_length_Std=('sepal_length', 'std'),petal_length_Mean=('petal_length', 'mean'), petal_length_Median=('petal_length', 'median'), petal_length_Std=('petal_length', 'std'),sepal_width_Mean=('sepal_width', 'mean'), sepal_width_Median=('sepal_width', 'median'), sepal_width_Std=('sepal_width', 'std'),petal_width_Mean=('petal_width', 'mean'), petal_width_Median=('petal_width', 'median'), petal_width_Std=('petal_width', 'std')))
Summary = df.groupby('species').agg(sepal_length_Mean=('sepal_length', 'mean'), sepal_length_Median=('sepal_length', 'median'), sepal_length_Std=('sepal_length', 'std'),petal_length_Mean=('petal_length', 'mean'), petal_length_Median=('petal_length', 'median'), petal_length_Std=('petal_length', 'std'),sepal_width_Mean=('sepal_width', 'mean'), sepal_width_Median=('sepal_width', 'median'), sepal_width_Std=('sepal_width', 'std'),petal_width_Mean=('petal_width', 'mean'), petal_width_Median=('petal_width', 'median'), petal_width_Std=('petal_width', 'std'))
Summary.to_csv('Summary.csv')