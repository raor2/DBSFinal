# DBSFinal
Final Project for Database Systems S19

Ryan, Daniel, Yang, Zhengneng

## Area to County Mapping
The Area column from the 'employmentData.csv' includes all counties from the NY state, which we will be directly using. 

- 'pull_Area.py' creates a 'Area_Remap.csv' that output the distinct 'Area' column in the 'employmentData.csv' file and replicate any indivisual county to 'County'.

However, some area are specified as two or three counties together, such as: 'Albany-Rensselaer-Schenectady Counties', 
In this case, we duplicate the data three times and categorized them as Albany County, Rensselaer County and Schenectady County respectively. 

- This part of the mapping was done by hand.

## Application Features

- Look up crime data based on the region (Area or County) or Year.

- Look up employment data based on the Industry (Coded in number Categories).

- Outputs the graph of crime rate history based on the region (Area or County).

- Outputs the graph of crime rate vs employment based on the region (Area or County).

- Outputs the best region(s) to live in based on user's preference on either low crime or high employment or somewhere in between. We devide the employment numbers by the crime numbers to obtain a ratio and use the ratio as the standard.

## User Instructions

### Creating Database and Loading Data

Creating and loading data is done in two steps

First, run the file dbsetup.sql as a super user in postgres

Then, run the file load_data.py and the database will be created, intialized and populated with data using the following information:

DB Name: 	finalproject

DB User: 	finalproject

DB password:	finalproject

## Application Instructions

### Execution


### Feature 1 & 2 - Raw Data Lookup (Area or County)
Feature 1 & 2 queries the raw data and plot the total crimes over the years based on Area or County. For example:
![alt text](https://github.com/raor2/DBSFinal/blob/master/Results_Graph/Feature1&2.jpg)

### Feature 3 - Employment Based on Industry
Feature 3 graphs the employment rate over the years, the data were then normalized for the purpose. The program prompt user to input the industry index. For example, if one inputs 'Real Estate and Rental and Leasing', the result is as follows:
![alt text](https://github.com/raor2/DBSFinal/blob/master/Results_Graph/Feature3.jpg)

### Feature 4 - Crime Rate & Employment Rate Based on Area
Feature 4 graphs the crime rate and employment rate over the years, the data were then normalized for the purpose. The program prompt user to input the area. For example, if one inputs 'Capital Area', the result is as follows:
![alt text](https://github.com/raor2/DBSFinal/blob/master/Results_Graph/Feature4.jpg)

### Feature 5 - Top NY Counties to Leave In
Feature 5 helps users to find the Best Counties to place their residency in based on their preference over the employment rate and the county's crime rate. User need to call the function 'TopCounties()'.

The program will prompt user to input:
- I. On a scale of 1-10, How much do you care about your future county's employment rate: 
and
- II. On a scale of 1-10, How much do you care about your future county's safety: 

For example, if one cares very much about the employment rate but not too much about the safety, one would input 10 to question 1 and input 1 to question 2, the program then will return the top 10 list:
![alt text](https://github.com/raor2/DBSFinal/blob/master/Results_Graph/Feature5.jpg)
 

