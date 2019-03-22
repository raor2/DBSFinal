
# Pull Distincts Area's for mannual remapping
import pandas as pd
df = pd.read_csv('employmentData.csv')
saved_column = list(set(df.Area))
saved_column.sort()

csv = open('Area_remap_duplicate.csv', "w") 
columnTitleRow = "Area, County\n"
csv.write(columnTitleRow)

for area in saved_column:
    row = area + "\n"
    row = row.replace(',',' ')
    if 'County' in area:
        row = area + "," + area + "\n"
    csv.write(row)

csv.close()
