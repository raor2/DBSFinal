import csv

crimeFile = open('crimeData.csv')
employmentFile = open('employmentData.csv')


crimes = crimeFile.read()
crimesHeading = "County,Agency,Year,Months,Report,Index Total,Violent Total,Murder,Rape,Robbery,Aggravated Assault,Property Total,Burglary,LarcenyMotor Vehicle Theft,Region"
#crimesHeading = crimesHeading.replace(",","\t")
#crimes = crimes.replace(",","\t")


print(crimesHeading)
print(crimes)
