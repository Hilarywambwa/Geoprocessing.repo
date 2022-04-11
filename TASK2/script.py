import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import mapclassify
#reading data
population = pd.read_csv(r"C:\Users\rana\Python programming\Spatial Data Analysis\Geoprocessing exercises\Task2\Data\County population.csv")
Primary_schools = pd.read_csv(r"C:\Users\rana\Python programming\Spatial Data Analysis\Geoprocessing exercises\Task2\Data\Primary_Schools.csv")
Kenya = gpd.read_file(r"C:\Users\rana\Python programming\Spatial Data Analysis\Geoprocessing exercises\Task2\Data\Kenya Admin Shapefiles\Counties.shp")
population.columns = ["County","Population"]
#Creating Geopandas Geodataframe
geometry = [Point(xy) for xy in zip(Primary_schools["x"], Primary_schools["y"])]
Primary_schools = gpd.GeoDataFrame(Primary_schools, geometry = geometry, crs = Kenya.crs)
#Renaming columns
Kenya.rename(columns = {"ADM1_EN":"County"}, inplace = True)
Kenya.index = Kenya['County']
Primary_schools.index = Primary_schools['Name of School']
Primary_schools = Primary_schools.drop(["Name of School"], axis=1)
#Spatial join
Primary_schools = gpd.sjoin(Primary_schools, Kenya, op = "within")
#Dropping unnecessary columns
Primary_schools.drop(columns=[
    'y', 'x', 'Level of Education', 'Status of School', 'Sponsor of School',
       'School Institution Type_1', 'School Institution Type_2',
       'School Institution Type_3', 'Pupil Teacher Ratio',
       'Pupil Classroom Ratio', 'Pupil Toilet Ratio',
       'Total Number of Classrooms', 'Boys Toilets', 'Girls Toilets',
       'Teachers Toilets', 'Total Toilets', 'Total Boys', 'Total Girls',
       'Total Enrolment', 'GOK TSC Male', 'GOK TSC Female',
       'Local Authority Male', 'Local Authority Female', 'PTA BOG Male',
       'PTA BOG Female', 'Others Male', 'Others Female',
       'Non-Teaching Staff Male', 'Non-Teaching Staff Female', 'Province',
       'District', 'Division', 'Location', 'index_right', 'Shape_Leng', 'Shape_Area',
    'ADM1_REF', 'ADM1ALT1EN', 'ADM1ALT2EN', 'ADM0_EN', 'ADM0_PCODE', 'date',
       'validOn', 'validTo'
])
#Obtaining number of primary schools in each county
grouped = Primary_schools.groupby('County').size()
Primary_schools = grouped.to_frame().reset_index()
Primary_schools.columns = ['County', 'count']
#Merging with population dataframe
DF = Primary_schools.merge(population, on = 'County')
#Calculating number of schools per 1000 people in each county
DF['Schools_per_1000'] = DF['count'] / (DF["Population"] / 1000)
#Merging counties and the new dataframe
Counties = gpd.read_file(r"C:\Users\rana\Python programming\Spatial Data Analysis\Geoprocessing exercises\Task2\Data\Kenya Admin Shapefiles\Counties.shp")
Counties.rename(columns = {"ADM1_EN":"County"}, inplace = True)
DF = Counties.merge(DF, on = 'County')
#Plotting
fig, ax = plt.subplots(figsize = (10, 8))
DF.plot(ax = ax, scheme='natural_breaks', k=5, cmap = "OrRd", edgecolor = "black", column = "Schools_per_1000",
       legend = True, legend_kwds={'loc': 'center left', 'bbox_to_anchor':(1,0.5)})
plt.title('Schools per 1000 in Kenya')
plt.savefig('C:/Users/rana/Python programming/Spatial Data Analysis/Geoprocessing exercises/Task2/Output/Map1.pdf')

