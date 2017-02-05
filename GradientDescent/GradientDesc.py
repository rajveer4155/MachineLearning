#####################################
#### Gradient Descent ML         ####
#### Author: Rajveer Sidhu       ####
#####################################
import sys
import random
import math
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

################### 
###Reading Labels##
###################
labelFile = sys.argv[2]
f = open(labelFile, 'r');
trainingLabels = {};
i = 0;
j = 0;
count = {};
count[0] = 0;
count[1] = 0;
l = f.readline();
while (l != ''):
    a = l.split();
    if (int(a[0]) == 0):
        trainingLabels[int(a[1])] = float(-1)
    else:
        trainingLabels[int(a[1])] = float(a[0])
    if int(a[0]) == 0:
        count[0] += 1;
    else:
        count[1] += 1;
    l = f.readline();
f.close()


### Defining Function for Dot product START
def getDotProduct(a, b):
    result = float(0);
    for i in range(0, len(a), 1):
        result += float(a[i] * b[i])
    #print("DP: ", result)
    return result


######################
### Initializing w ###
######################
eta = .001;
w = []

for i in range(0, cols, 1):
    w.append(2 * eta * random.random() - eta)

currentObj = float(0)
for i in range(0, rows, 1):
    if (trainingLabels.get(i) != None):
        dp = getDotProduct(w, data[i])
        currentObj += (trainingLabels[i] - dp) ** 2



i = 0

prevObj = float("inf")
currentObj = float(0)
itr = 1;
############################
### Starting Convergence ###
############################
while (prevObj - currentObj > 0):
    dellf = []
    for k in range(0, cols, 1):
        dellf.append(0.0)
    if currentObj:
        prevObj = currentObj
    else:
        prevObj = float("inf")
    currentObj = float(0)
    for i in range(0, rows, 1):
        if (trainingLabels.get(i) != None):
            dp = getDotProduct(w, data[i])
            for j in range(0, cols, 1):
                dellf[j] += (trainingLabels.get(i) - dp) * data[i][j]

    # updating DellF
    for j in range(0, cols, 1):
        w[j] = w[j] + eta * dellf[j]

    # Calculating new gradient
    for i in range(0, rows, 1):
        if (trainingLabels.get(i) != None):
            dp = getDotProduct(w, data[i])
            currentObj += (trainingLabels[i] - dp) ** 2
    itr += 1

print("Converged w: ", w)
print("Converged on iteration: ",itr)

### Calculating distance from the origin ###

normw = float(0.0)

for i in range(0, cols - 1, 1):
    normw += w[i] ** 2
normw = math.sqrt(normw)

dOrigin = abs(w[len(w) - 1] / normw)
print("distance=", dOrigin)


##################
### Predicting ###
##################
file = open("predictions_gradDesc.txt", "w")
for i in range(0,rows,1):
		if(trainingLabels.get(i) == None):
			dp=float(0);
			dp= getDotProduct(w,data[i])
			if(dp<0):
				#print("Point ",i,":",0)
				file.write("0 "+ str(i)+"\n")
			else:
				#print("Point ",i,":",1)
				file.write("1 "+ str(i)+"\n")

















