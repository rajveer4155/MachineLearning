########################################
#### K-Means Clustering             ####
#### Author: Rajveer Sidhu          ####
########################################
import sys
import random
import pdb

###################
###Reading Data ###
###################
dataFile = sys.argv[1];
f = open(dataFile, 'r');
data = [];
i = 0;
j = 0;
l = f.readline();
while (l != ''):
    a = l.split();
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]));
    l2.append(float(1));
    data.append(l2);
    l = f.readline();
rows = len(data);
cols = len(data[0]);
	
print(data);
def getDistance(a,b):
	result = 0
	for i in range(0, len(a), 1):
		result += (a[i]-b[i])**2
	return result**0.5

######################################
### Initializing mean for clusters ###
######################################

# K= number of clusters
k = int(sys.argv[2])		

clusters = []
mean = []

### Associating data points to means with equal probability
randSample = random.sample(data,k)

#print("Rand Sample:",randSample);
### sampling clusters randomly
for temp in randSample:
	sampledData =[]
	for val in temp:
		sampledData.append(val)		
	mean.append(sampledData)
#print("Sample Data:",sampledData);
#print("Mean Sample:",mean);
### Initializing Clusters 

minDist = float("inf")
clusterLabel = 0

tempClusters = []
for i in range(0, k, 1):
	tempClusters.append(0)

for i in range(0, rows, 1):
	minDist = float("inf")
	clusterLabel = 0
	for j in range(0, k, 1):
		distance = getDistance(data[i],mean[j])
		if (distance < minDist):
			clusterLabel = j
			minDist = distance
        #Associating data point to cluster
	clusters.append(clusterLabel)				
	tempClusters[clusterLabel] += 1


######################################
### Starting final mean calcs      ###
######################################

for i in range(0, k, 1):
	for j in range(0, cols, 1):
		mean[i][j] = 0

for i in range(0, rows, 1):
	mean[clusters[i]] = [x + y for x, y in zip(mean[clusters[i]],data[i])]

for j in range(0, k, 1):
	if(tempClusters[j] != 0):
		temp = [x / tempClusters[j] for x in mean[j]]
	else:
		temp = [0 for x in mean[j]]

	mean.pop(j)
	mean.insert(j,temp)

######################################
### Starting Minimizing Objective  ###
######################################

### Initializing Objective

currentObj = 0.0
for i in range(0, rows, 1):
	currentObj += getDistance(data[i],mean[clusters[i]])

### Minimizing

prevObj = float("inf")

while(prevObj - currentObj > 0.01):

	prevObj = currentObj
	minDist = float("inf")
	clusterLabel = 0
	
	#Clustering
	tempClusters = []
	for i in range(0, k, 1):
		tempClusters.append(0)

	for i in range(0, rows, 1):
		minDist = float("inf")
		clusterLabel = 0
		for j in range(0, k, 1):
			distance = getDistance(data[i],mean[j])
			if (distance < minDist):
				clusterLabel = j
				minDist = distance
		clusters[i] = clusterLabel				
		tempClusters[clusterLabel] += 1

	### new mean calcuation for current Obj

	for i in range(0, k, 1):
		for j in range(0, cols, 1):
			mean[i][j] = 0

	for i in range(0, rows, 1):
		for j in range(0, cols, 1):
			mean[clusters[i]][j] += data[i][j]

	for j in range(0, k, 1):
		if(tempClusters[j] != 0):
			temp = [x / tempClusters[j] for x in mean[j]]
		else:
			temp = [0 for x in mean[j]]
		
		mean.pop(j)
		mean.insert(j,temp)	

	### Calculating new objective 

	obj = 0.0
	for i in range(0, rows, 1):
		currentObj += getDistance(data[i],mean[clusters[i]])

######################################
###   Writing Output to Clusters   ###
######################################
file = open("kmeansClusters.txt", "w")
for i in range(0, rows, 1):
	#print(i," ",clusters[i])
	file.write(str(clusters[i])+" "+str(i)+"\n")

