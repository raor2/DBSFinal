import psycopg2
import psycopg2.extras
import matplotlib.pyplot as plt
import numpy as np
#Outputs the graph of crime rate vs employment 
#based on the region ( County)




#def CrimeVSEmployment(InputArea):

def CrimeAndEmployment(InputCounty):
    connection_string = "host='localhost' dbname='finalproject' user='finalproject' password='finalproject'"
    conn = psycopg2.connect(connection_string, cursor_factory=psycopg2.extras.DictCursor)
    cursor = conn.cursor()
    cursor.execute("SELECT county FROM AreaLookup;")	
    county = cursor.fetchall()
    assert ([InputCounty] in county)
    #FIND employment 
    cursor.execute("SELECT W.year, SUM(CAST (W.avgEmployment AS int))\
    		FROM AreaLookup A, Wages W \
    		WHERE A.county = %s \
    			AND A.area = W.area \
    		GROUP BY W.year	\
            ORDER BY W.year ASC",(InputCounty,))
    employment = cursor.fetchall()
    employment = np.array(employment)
    #FINF crime
    cursor.execute("SELECT c.year, SUM( CAST(c.totalcrimes AS int))\
        FROM data.countylookup cl, data.crime c\
        WHERE cl.county=%s \
        	AND cl.agency = c.agency\
        	AND c.totalcrimes <> ''\
        GROUP BY c.year\
        ORDER BY c.year ASC",(InputCounty,))
    crime = cursor.fetchall()
    crime = np.array(crime)
    #PLOT
    
    x = crime[:,0] 
    y = crime[:,1]
    plt.plot(x, y) 
    plt.xlabel('x - axis') 
    plt.ylabel('y - axis') 
    plt.title('crime') 
    plt.rcParams["figure.figsize"] = [16,9]
    plt.show() 
    
    x = employment[:,0] 
    y = employment[:,1]
    plt.plot(x, y) 
    plt.xlabel('x - axis') 
    plt.ylabel('y - axis') 
    plt.title('employment') 
    plt.show() 
    
