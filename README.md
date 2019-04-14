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

### Application Instructions
 

