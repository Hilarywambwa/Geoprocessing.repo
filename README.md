**TASK1**

A python script that outputs the schools connected and schools not connected to roads in Dagoretti South constituency in Kenya.
DATA:
**constituency shapefile,
roads shapefile,
schools shapefile,**
Geoprocessing tool used is **BUFFER** and **INTERSECTION** where schools intersecting with a 15m road are considered connected to a road whereas those not intersecting with the 15m road buffer are considered not connected.

**TASK2**
A python script that outputs a chrolopleth map showing the number of primary schools per 100 people in Kenyan counties.
DATA:
Kenyan counties shapefile,
Population data in CSV format,
Primary_schools in CSV format,
Geoprocessing tool used is **SPATIAL JOINS** to determine the primary schools within each constituency.
