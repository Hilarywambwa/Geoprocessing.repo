import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from shapely.geometry import Point

#Importing data
SA1 = gpd.read_file(r"C:\Python\Data\10 Geoprocessing applications\Study_Area_1.shp")
SA2 = gpd.read_file(r"C:\Python\Data\10 Geoprocessing applications\Study_Area_2.shp")
river = gpd.read_file(r"C:\Python\Data\10 Geoprocessing applications\river.shp")
fig,ax = plt.subplots()
SA1.plot(ax=ax, color="blue", edgecolor="black")
SA2.plot(ax=ax, color="none", edgecolor="black")
river.plot(ax=ax)

#Intersection of polygons
Intersection = gpd.overlay(SA1, SA2, how="intersection")
Intersection.plot()

#Intersection of polygons
Union = gpd.overlay(SA1, SA2, how="union")
Union.plot()
Union

#Symmetric difference of polygons
Sd = gpd.overlay(SA1, SA2, how="symmetric_difference")
Sd.plot()

#Difference of polygons
Difference = gpd.overlay(SA1, SA2, how="difference")
Difference.plot()

#Dissolve Polygons
union = gpd.overlay(SA1, SA2, how="union")
union["commoncol"]=1
union
dissolved_sa = union.dissolve(by = "commoncol")
dissolved_sa.plot()
dissolved_sa

#Buffer
river.crs
#Project coordinate system to buffer in meters
river_projected = river.to_crs(24547)
river_projected.plot()
buffer_500 = river_projected["geometry"].buffer(distance=500)
buffer_500.plot()

#Obtaining a centroid
UNION = gpd.overlay(SA1, SA2, how="union")
UNION.plot(edgecolor="black")
centroid = UNION["geometry"].centroid
centroid.plot()
fig1,ax1 = plt.subplots()
UNION.plot(ax=ax1, color="blue", edgecolor="black")
centroid.plot(ax=ax1, color="black")

#Attribute joins
us_states = gpd.read_file(r"C:\Python\Data\10 Geoprocessing applications\us_states.shp")
airports = pd.read_csv(r"C:\Python\Data\10 Geoprocessing applications\us_airports.csv")
states_names_codes = pd.read_csv(r"C:\Python\Data\10 Geoprocessing applications\state names and codes.csv")
geometry = [Point(xy) for xy in zip(airports["LONGITUDE"], airports["LATITUDE"])]
us_airports = gpd.GeoDataFrame(airports, geometry = geometry, crs=us_states.crs)
#Renaming column heading
us_airports.rename(columns = {"STATE":"state_code"}, inplace = True)
us_airports.columns
#Attribute joins
us_airports = us_airports.merge(states_names_codes, on = 'state_code')
us_airports

#Spatial joins
us_airports = us_airports[["AIRPORT", "geometry"]]
fig2, ax2 = plt.subplots(figsize=(8,8))
us_states.plot(ax = ax2, color="blue", edgecolor="black")
us_airports.plot(ax = ax2, color="green")
us_airports = gpd.sjoin(us_airports, us_states, how="inner", op='intersect')
