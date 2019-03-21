
# Pull Distincts Area's for mannual remapping
import pandas as pd
df = pd.read_csv('employmentData.csv')
saved_column = list(set(df.Area))

csv = open('Area_remap.csv', "w") 
columnTitleRow = "Area, County\n"
csv.write(columnTitleRow)

for area in saved_column:
	row = area + "\n"
        print(row)
        csv.write(row.replace(',',' '))

