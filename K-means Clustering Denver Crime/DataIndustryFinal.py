# Christopher Seven
# Data Analysis in the Industry

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import cluster
import scipy
from scipy.cluster.vq import vq
import folium
import webbrowser

pd.options.mode.chained_assignment = None  # default='warn'

# Reading in the data as a csv file and dropping missing values.
dataset = pd.read_csv(r'C:\Users\Chris\PycharmProjects\COMP3005\crime.csv')
dataset = dataset.dropna()

# Picking specific columns and renaming them.
totaldataset = dataset.loc[dataset['OFFENSE_CATEGORY_ID'].isin(["burglary", "auto-theft", "aggravated-assault", "murder", "arson"])]
totaldata = totaldataset[["INCIDENT_ID", "OFFENSE_TYPE_ID", "OFFENSE_CATEGORY_ID", "FIRST_OCCURRENCE_DATE", "GEO_LON", "GEO_LAT", "NEIGHBORHOOD_ID", "INCIDENT_ADDRESS"]]
totaldata.columns = ("ID", "Offense Type", "Offense Category", "Timestamp", "Longitude", "Latitude", "Neighborhood", "Address")

X = totaldata[["Latitude","Longitude"]]

# Calculating the distortion at each k value from 1 to 10 with 300 iterations.
distortionList = []
for i in range(1, 11):
    if len(X) >= i:
       tempKmean = cluster.KMeans(n_clusters=i, init='k-means++', n_init=10, random_state=0)
       tempKmean.fit(X)
       distortionList.append(tempKmean.inertia_)

k_optimal = 6

# Plotting the elbow method results.
fig, ax = plt.subplots()
ax.plot(range(2, len(distortionList)+1), distortionList[1:])
ax.set(title='The Elbow Method', xlabel='K', ylabel="Distortion")
ax.axvline(k_optimal, ls='-', color="blue")
ax.grid(True)
plt.show()

Kmean_model = cluster.KMeans(n_clusters=k_optimal, init='k-means++')

X["cluster"] = Kmean_model.fit_predict(X)

# Calculating the centroids, and adding the points that are centroids to the dataset.
centroidVal, dist = scipy.cluster.vq.vq(Kmean_model.cluster_centers_, X.drop("cluster", axis=1).values)
X["centroids"] = 0
for i in centroidVal:
    X["centroids"].iloc[i] = 1
totaldata[["cluster","centroids"]] = X[["cluster","centroids"]]

# Mapping Denver in folium.
lat, long = 39.7392364, -104.9848623
x, y = "Latitude", "Longitude"

data = totaldata.copy()

denvermap = folium.Map(location=[lat, long])

# Assigning colors to each cluster.
clustersList = sorted(list(totaldata["cluster"].unique()))
colorsList = ['#%06X' % np.random.randint(0, 0xFFFFFF) for i in
              range(len(clustersList))]
data["color"] = data["cluster"].apply(lambda x:
                colorsList[clustersList.index(x)])

# Specifically marking the centroids.
centroidsList = sorted(list(data["centroids"].unique()))
data[data["centroids"]==1].apply(lambda row:
           folium.Marker(location=[row[x],row[y]],
           popup=row["centroids"], draggable=False,
           icon=folium.Icon(color="black")).add_to(denvermap), axis=1)

# Adding the crime data points to the map.
coordlist = []
for i in range(len(totaldata["Longitude"])):
    coordlist.append((float(totaldata.iloc[i, 5]), float(totaldata.iloc[i, 4])))
    folium.CircleMarker(location = coordlist[i], popup = data.iloc[i, -4], radius = 3, color = data.iloc[i, -1]).add_to(denvermap)
print(totaldata)
# Opening the map as an html.
denvermap.save("map_1.html")
webbrowser.open("map_1.html")

