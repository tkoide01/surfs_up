# Surfs Up Analysis
Utilize SQLite and Python to analyze temperature data
## Overview of the Project
Using SQLite data and Python to determine whether opening a surf and ice cream shop business in Oahu would be sustainable year-round. In order to determine that business decision, we will find summary statistics of temperature data by outputting the following technical analysis and a written report:

Deliverable 1: Determine the Summary Statistics for June
Deliverable 2: Determine the Summary Statistics for December
Deliverable 3: A written report for the statistical analysis

## Resources
- Data Source: hawaii.sqlite
- Used code: SurfsUp_Challenge.ipynb
- Software: Visaul Studio Code, Jupytor Note Book

## Results
  Based on the two technical analysis summarizing the temperature of June and December in Oahu, we can find followings differences in weather between June and December.
  
*** Summary Statistics of June Temperature in Oahu ***
  
   ![](Images/june_temp_summary.png)
   
*** Summary Statistics of December Temperature in Oahu ***
  
   ![](Images/dec_temp_summary.png)

   
  1. Comparing the two summary statistics above, we can find that the temperature of December is in average 3.9 degrees in fahrenheit lower compared to the temperature of June. Given the mean temperature of both June and December in Oahu is above 71 degrees, it seems that Oahu is suitable for surfing and ice cream business year-round if we only focus on this information.
  2. The max temperature of both June and December are ranged between 83 and 85 degrees. This is not exceedingly hot for surfing activity.
  3. On the other hand, the minimum temperature in December is 56 degrees. This would be too cold for both surfing and ice cream business, and thus we should make additional gathering of data to measure how often the cold weather occurs in December.
  
## Summary
   In addition to above observations, we delivered a few additional queries to gather more weather information for June and December. 
   In order to determine "What temperature would be **too** cold for surfing," I researched 

  1. First of all, we run queries to visualize how temperature data is spread in June and December.
  
   First of all, we create two DataFrames for June temperature and December temperature.
  *** Query for June Temperature DataFrame *** 
  ```
  june = "06"
  results_june = []
  results_june = session.query(Measurement.date, Measurement.tobs).\
      filter(func.strftime("%m",Measurement.date) == june).all()
  df_06 = pd.DataFrame(results_june, columns = ['date','temperature'])
 ```
 *** Query for December Temperature DataFrame *** 
 ```
  dec = "12"
  results_dec = []
  results_dec = session.query(Measurement.date, Measurement.tobs).\
      filter(func.strftime("%m",Measurement.date) == dec).all()
  df_12 = pd.DataFrame(results_june, columns = ['date','temperature'])
```
   Then, run below queries to plot temperature data in histogram.
```
  df_06.plot.hist(bins=20)
  and 
  df_12.plot.hist(bins=20)
```
  
   ![](Images/june_temp_histogram.png)
   ![](Images/dec_temp_histogram.png)

  3. Plan special promotions for both Drivers and Riders to improve the supply and demand balance of ride based on the trend we see in the multiple-line chart.
    
  
