DROP SCHEMA IF EXISTS data CASCADE;
CREATE SCHEMA data;


CREATE TABLE CountyLookup(
	County VARCHAR(64) NOT NULL,
	Agency VARCHAR(128) NOT NULL,
	PRIMARY KEY(Agency),
	FOREIGN KEY(County) REFERENCES AreaLookup(County)

);


CREATE TABLE AreaLookup(
	Area VARCHAR(64) NOT NULL,
	County VARCHAR(64) NOT NULL,
	PRIMARY KEY(County),
	FOREIGN KEY(County) REFERENCES CountyLookup(County)
	FOREIGN KEY(Area) REFERENCES AreaTypeLookup(Area)
	
);

CREATE TABLE AreaTypeLookup(
	Area VARCHAR(64) NOT NULL,
	AreaType VARCHAR(64) NOT NULL,
	PRIMARY KEY(Area),
	
);

CREATE TABLE NAICSLookup(
	NAICS INTEGER NOT NULL,
	NAICSTitle VARCHAR(128) NOT NULL
);

CREATE TABLE Wages(
	Area VARCHAR(64) NOT NULL,
	NAICS INTEGER NOT NULL,
	Year INTEGER NOT NULL,
	numEstablishments INTEGER NOT NULL,
	avgEmployment INTEGER NOT NULL,
	totalWage INTEGER NOT NULL,
	annualAvgSalary INTEGER NOT NULL,
	PRIMARY KEY(Area, NAICS, Year),
	FOREIGN KEY(Area) REFERENCES AreaTypeLookup(Area),
	FOREIGN KEY(NAICS) REFERENCES NAICSLookup(NACIS),
	FOREIGN KEY(Area) REFERENCES AreaLookup(Area)
);

CREATE TABLE Crime(
	Agency VARCHAR(128) NOT NULL,
	Year INTEGER NOT NULL,
	MonthsReportedForCrime INTEGER NOT NULL,
	totalCrimes INTEGER,
	totalViolentCrimes INTEGER,
	murderCrimes INTEGER,
	rapeCrimes INTEGER,
	robberyCrimes INTEGER,
	aggravatedAssaultCrimes INTEGER,
	totalPropertyCrimes INTEGER,
	burgalaryCrimes INTEGER,
	larcenyCrimes INTEGER,
	motorVehicleTheftCrimes INTEGER,
	PRIMARY KEY(Agency,Year),
	FOREIGN KEY(Agency) REFERENCES CountyLookup(Agency)	
);

