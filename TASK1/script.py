import geopandas as gpd
import matplotlib.pyplot as plt

#Reading the Data
Constituency = gpd.read_file(r"C:\Users\rana\Python programming\Spatial Data Analysis\Geoprocessing exercises\Task1\Data\Dagoretti_south.shp")
roads = gpd.read_file(r"C:\Users\rana\Python programming\Spatial Data Analysis\Geoprocessing exercises\Task1\Data\roads.shp")
schools = gpd.read_file(r"C:\Users\rana\Python programming\Spatial Data Analysis\Geoprocessing exercises\Task1\Data\schools.shp")
#Reprojecting Data
Constituency = Constituency.to_crs(epsg = 21037)
roads = roads.to_crs(epsg = 21037)
schools = schools.to_crs(epsg = 21037)
#Creating a 15 meter buffer on all roads. All schools within 15 meter buffer are considered connected to the road
buffer_15 = roads["geometry"].buffer(distance = 15)
buffer = buffer_15.to_crs(epsg = 21037)
buffer = gpd.GeoDataFrame(geometry=gpd.GeoSeries(buffer)) 
Schools_connected_to_roads = gpd.overlay(buffer, schools, how ="intersection", keep_geom_type=False)
#Plotting
fig, ax = plt.subplots(figsize = (35,25))
Constituency.plot(ax = ax, edgecolor = "black", color = 'None',label = "Constituency")
roads.plot(ax = ax, color = "brown", label = 'roads')
schools.plot(ax = ax, markersize = 25, color = "red", label = 'Schools not connected to roads')
Schools_connected_to_roads.plot(ax = ax, markersize = 25, color = "green", label = "Schools connected to roads")
plt.legend(handleheight = 5)
plt.title('Dagoretti South Constituency', fontsize = 25)
#Naming
for x, y, label in zip(schools.geometry.x, schools.geometry.y, schools.Name):
    ax.annotate(label, fontsize = 5, xy=(x, y), xytext=(3, 3), textcoords="offset points")
plt.savefig('C:/Users/rana/Python programming/Spatial Data Analysis/Geoprocessing exercises/Task1/Output/Map.pdf')