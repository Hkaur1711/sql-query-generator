# sql-query-generator
Using NLP and ML/DL to process human questions and convert them to SQL queries that can be executed to get results from database

## Procedure
For any given input, these are the steps that I followed:
##### Phase 1: Query Parser - Get insights from the question
1. Column Name: Find the column name specified in the query(say sales)
2. Value  : Value of the f0
3. Table/Database name it belongs to.
4. Identify the stop words like (is, in, on, the, at) and neglect it.
5. Identify the question words
    * What/who – portrait
    * When – Timeline
    * How – Flow Chart
    * Why – Multiple variable plot
    * Where – Map
    * How Much – Bar Chart
    * How long – TimeLine
    * How Far- 
6. Finding the analytical keywords
    * Correlation
    * Maximum
    * Minimum
    * Median
    * Mode
    * Cross correlation
    * Variance
    * Expectation
7. Find the ML Keywords 
    * Predict
    * Visualize
    * Cluster
    * Time trend analyse
    * Analyse
    * Detect
    * Classify
    * Regression
8. Chart Names:
    * Bar chart
    * Pie Chart
    * Scatter Plot
    * Heat Map
    * Line Chart
    * Histogram
    * TimeLine Chart
    * Flow Chart
    * Tree Chart
    * Area Chart
    * Cartogram
    * Bubble chart
9. Keywords:
    * Top Most
    * Going Good
    * Least
    * Worst
    * Best
    * Surprisingly well
    * Satisfactory
    * Unsatisfactory
    * Currently Moving well
    * Currently not moving well
    * Currently top
10. Time Functions
    * Last Month
    * Last Year
    * Last quarterly
    * Last half yearly
    * Last year
    * Daily
    * Particular(date)
    * Yesterday
    * Today
    * Last week
    * Current week
    * Current month
    * Recently
    * Monthly
    * Yearly
    * Weekly

#### Phase 2 - Auto Analyzer - Possible operations of auto analyzer
* Outlier Detection( using Z-Scores and algorithms like SVM,SOM)
* Classification
* Clustering
* Recommendation System
* Min Max
* Covariance and Expectation
* Regression(linear or Multilinear)
* Correlation
* Cross correlation
* Mean Median Mode
* Sum
* Average
* Prediction
* Trend Analysis
* Pattern recognition

#### Phase 3 - Visualization - Possible chart types

![image](https://user-images.githubusercontent.com/63356527/109384359-375ac580-7912-11eb-88ce-dd84171f75e9.png)

## Flow Chart

![image](https://user-images.githubusercontent.com/63356527/109384381-56f1ee00-7912-11eb-80d2-da38417313bf.png)


## Example

![image](https://user-images.githubusercontent.com/63356527/109384391-683afa80-7912-11eb-9405-026fdc668a8c.png)


