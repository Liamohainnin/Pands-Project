Analysis

Analysis.py is a python script for the automated analysis and plotting of the Fishers Iris dataset. This dataset has been a key dataset for many statistical classification techniques in machine learning and data analytics.
Fishers Iris Dataset is well known multivariate dataset often used to demonstrate a linear discriminant analysis.
The data was actually collected by Edgar Anderson an American Botonist and consists of data from 3 species of Iris,
Iris Sertosa, Iris Versicolor and Iris Virginica. 

The Iris Flower data is divided into a number of categories, Petal Width, Petal Length, Sepal width and Sepal width and measurements were taken in cm's. 
Through an analysis of these values together it is possible to differentiate between the Iris Sertosa and the other 2 species based on the values of Petal length and width.

The initial plotting of the values results in a clear delineation of the Sertosa speicimens through its distinct values for Petal length and width however there is a bit more overlap 
between the other 2 species. The linear discriminant analysis techinque employed by fisher allowed for clearer delineation of the other 2 species by transforming the values and replotting
them relative to another axis which allowed for clearer delineation of the 2 datasets. I have not gone down this route in the current project but this would be logical nest step in taking 
the analysis of the dataset further as has been described in detail at the towardsdatascience reference below.

The analysis.py script does however produce an additional aggregation of the Iris datasets variables grouping the records by species type and producing group mean,median and standard deviation.

species	   sepal_length_Mean	sepal_length_Median	sepal_length_Std	     petal_length_Mean	petal_length_Median	petal_length_Std	sepal_width_Mean	sepal_width_Median	sepal_width_Std	petal_width_Mean	petal_width_Median	petal_width_Std
setosa	    5.006                      5	            0.352489687213451	      1.464	              1.5	          0.173511159436445  	3.418	             3.4	           0.381024397954691	0.244	0.2	0.107209503081678
versicolor	5.936	                  5.9	            0.516171147063863	      4.26	              4.35	          0.469910977239958	    2.77	             2.8	           0.313798323378411	1.326	1.3	0.197752680004544
virginica	6.588	                  6.5	            0.635879593274432	      5.552	              5.55	          0.551894695663983	    2.974	             3	               0.322496638172638	2.026	2	0.274650055636667

Here are the aggregated stats not grouped/ broken down by species as produced by the data frame describe data summary operatation.
	     sepal_length	sepal_width	petal_length	petal_width
count	     150	        150	       150	           150
mean	     5.843333	   3.054	    3.758667	     1.198667
std	         0.828066	  0.433594	  1.76442	     0.763161
min	         4.3	         2	        1	            0.1
25.00%	     5.1	        2.8	       1.6	            0.3
50.00%	     5.8	         3	       4.35         	1.3
75.00%      	6.4     	3.3	        5.1	            1.8
max	            7.9	        4.4	        6.9	            2.5

https://archive.ics.uci.edu/ml/datasets/iris

https://towardsdatascience.com/linear-discriminant-analysis-in-python-76b8b17817c2

TR. A. Fisher (1936). "The use of multiple measurements in taxonomic problems". Annals of Eugenics. 7 (2): 179–188.
Installation
Edgar Anderson (1935). "The irises of the Gaspé Peninsula". Bulletin of the American Iris Society. 59: 2–5

Copy the analysis.py and the Iris.csv file script into a folder. 
you may run the scrtipt using any of the methods outlined at url below.
https://realpython.com/run-python-scripts/

Usage

Reads the Iris.csv file into data frame.
Plots all variables as Histograms.
Save plots of all variables to png file in local directory.
Generates a summary of all the variables in the Iris Dataset.
Exports summary of all the variables in the Iris Dataset to csv file .
Generates scatterplot of each pair of variables in the Iris Dataset
Saves scatterplot of each pair of variables to png file in local directory.
Generates a summary of all the variables in the Iris Dataset grouped by Species.
Outputs a Horizontal bar chart of the variables with sub plots showing variables grouped by species together to a png file in local directory. 


Contributing

At this stage we do not anticipate any further contributions being required.
License

MIT
