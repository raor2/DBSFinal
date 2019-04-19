SELECT cl.County 
FROM Wages w, Crime c, CountyLookup cl,AreaLookup al 
WHERE c.Agency = cl.Agency AND cl.County = al.County 
AND w.Year = c.Year AND w.Year = 2017 AND c.Year = 2017 AND c.totalCrimes <> '' 
GROUP BY cl.County
LIMIT 100;