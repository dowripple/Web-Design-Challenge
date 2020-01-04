# Web-Design-Challenge
## by Michael Dowlin
### 1/4/20

!['Image not available'](/Resources/assets/images/Fig1.png)

#### Link to Live Site
[Web-Design Site Link](https://dowripple.github.io/Web-Design-Challenge/)

#### Description
The purpose of this project was to analyze how weather changes as you get closer to the equator. 
To accomplish this analysis, we first pulled data from the OpenWeatherMap API to assemble a dataset on over 500 cities.
After assembling the dataset, we used Matplotlib to plot various aspects of the weather vs. latitude.  Factors we looked at included: temperature, cloudiness, wind speed, and humidity.  
This site provides the source data and visualizations created as part of the analysis, as wells as explanations and descriptions of any trends and correlations witnessed.

To create a new data table (table.html), run the convertTable.py function in the project root.  The index.html page is the home page for the project.

#### Contents

| File                         | Description                                                                                     |
|------------------------------|-------------------------------------------------------------------------------------------------|
|cloudiness.html               | html page to show Cloudiness vs Latitude analysis
|comparisons.html              | html page that shows all for analysis scatter charts
|convertTable.py               | python program that will convert the cities.csv file into an html document
|data.html                     | page to show an html table representation of the cities.csv file (pulled in via js)
|humidity.html                 | html page to show the humidity vs Latitude analysis
|index.html                    | main html page, all other pages can be navigated to from here
|maxTemp.html                  | html page to show the max temp vs. Latitude analysis
|table.html                    | the output of the "convertTable.py", run that program manually to recreate the file
|windspeed.html                | html page to show Wind Speed vs Latitude analysis
