#Using QgsDistanceArea to compute distances and areas
Bungoma = (0.5695, 34.5584)

Nairobi = (1.2921, 36.8219)

#create an object by instantiating it
d = QgsDistanceArea()

 #set the ellipsoid 
d.setEllipsoid('WGS84')

#All valid ellipsoids can be found by calling QgsEllipsoidUtils.acronyms()
#Use measureLine() method. This method takes a list QgsPointXY objects
point1 = QgsPointXY(34.5584, 0.5695)

point2 = QgsPointXY(36.8219, 1.2921)

#convertLengthMeasurement() converts the measured distance to any supported unit. 
#It takes 2 arguments - the length measured by measureLine() method and the unit to convert the measurement to
distance = d.measureLine([point1, point2])
print('Distance in meters', distance)

distance_km = d.convertLengthMeasurement(distance, QgsUnitTypes.DistanceKilometers)
print('Distance in kilometers', distance_km)

distance_mi = d.convertLengthMeasurement(distance, QgsUnitTypes.DistanceMiles)
print('Distance in miles', distance_mi)