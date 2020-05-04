Analysis

Analysis.py is a python script for the automated analysis and plotting of the Fishers Iris dataset. This dataset has been a key dataset for many statistical classification techniques in machine learning and data analytics.
Fishers Iris Dataset is well known multivariate dataset often used to demonstrate a linear discriminant analysis.
The data was actually collected by Edgar Anderson an American Botonist and consists of data from 3 species of Iris,
Iris Sertosa, Iris Versicolor and Iris Virginica. 

The Iris Flower data is divided into a number of categories, Petal Width, Petal Length, Sepal width and Sepal width and measurements were taken in cm's. 
Through an analysis of these values together it is possible to differentiate between the Iris Sertosa and the other 2 species based on the values of Petal length and width.

The initial plotting of the values results in a clear delineation of the Sertosa specimens through its distinct values for Petal length and width however there is a bit more overlap 
between the other 2 species. The linear discriminant analysis techinque employed by fisher allowed for clearer delineation of the other 2 species by transforming the values and replotting
them relative to another axis which allowed for clearer delineation of the 2 datasets. I have not gone down this route in the current project but this would be logical nest step in taking 
the analysis of the dataset further as has been described in detail at the towardsdatascience reference below.

The analysis.py script does however produce an additional aggregation of the Iris datasets variables grouping the records by species type and producing group mean,median and standard deviation.

 |species|Sepal_len_Mean|Sepal_len_Med|Sepal_len_Std|Petal_len_Mean|Petal_len_Med|Petal_len_Std|Sepal_Wid_Mean| 	Sepal_width_Med|Sepal_width_Std|Petal_wid_Mean|Petal_wid_Med|Petal_wid_Std| 
 -------------------------------------------------------------------------------------------------------------------------
 | setosa	 | 5.006  | 5	| 0.3524 | 1.464  | 1.5	 |  0.1735 |	3.418	 |  3.4	 | 0.3810 | 	0.244 | 	0.2 |	0.1072 | 
 
 | versicolor | 	5.936	  |  5.9	 | 0.5161	 |  4.26 |  4.35	 |  0.4699 | 2.77 |  2.8	 |  0.3137	 | 1.326	 | 1.3	0.1977 | 
 
 | virginica | 	6.588	 |   6.5	  |  0.6358	  |  5.552	 | 5.55	|   0.5518	 |  2.974	 | 3	 | 0.3224	| 2.026 | 	2	 | 0.2746 | 

Here are the aggregated stats not grouped/ broken down by species as produced by the data frame describe data summary operation.

  ---     | sepal_length | sepal_width | petal_length | petal_width|
 ----------------------------------------------------------------------
 | count	 |   150	   |   150	|   150	 |   150 |
 
 | mean	  |   5.8433 | 3.054	| 3.7586	|  1.1986|
 
 | std	   |  0.8280  | 0.4335	| 1.764 |   0.7631|
 
 | min	   |   4.3	   |  2	   |  1  |  0.1|
 
 | 25.00%	|   5.1	   |  2.8	 | 1.6	 |  0.3|
 
 | 50.00%	|   5.8	   |   3   | 4.35 | 	1.3|
 
 | 75.00% |  	6.4    | 3.3	  | 5.1  |  1.8|
 
 | max	   |   7.9	   |   4.4	|  6.9	|  2.5|

References 

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
