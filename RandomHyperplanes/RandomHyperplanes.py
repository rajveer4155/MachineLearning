#########################################
####  Random Hyperplanes             ####
####  Author: Rajveer Sidhu          ####
#########################################
import sys
import random
import math
import pdb
from sklearn import svm

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
    #l2.append(float(0));
    data.append(l2);
    l = f.readline();
rows = len(data);

#print("rows: ",rows,"cols: ",cols)
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

#print("Row 1", data[1])


### Defining Function for Dot product START
def signOfDotProduct(a, b):
    result = float(0);
    for i in range(0, len(a), 1):
        result += float(a[i] * b[i])
    #print("DP: ", result)
    if(result>=0):
        return 1
    else:
        return -1

### Defining Function for Dot product START
def getDotProduct(a, b):
    result = float(0);
    for i in range(0, len(a), 1):
        result += float(a[i] * b[i])
    # print("DP: ", result)
    return result

#####
def getModVector(a):
    normw=float(0);
    for i in range(0, cols - 1, 1):
        normw += a[i] ** 2
        return normw

#### Get a random w
def getRandomW(dimen):
    w=[]
    for i in range(0,dimen,1):
        w.append(random.uniform(-1,1))
    return w

def ScikitSVM(x,y):
    z1 = []
    zlabels = []
    z2 = []
    zOrigRows=[]

    for i, zi in enumerate(x):
        yi = y.get(i)
        if yi is None:
            z2.append(zi)
            zOrigRows.append(i)
        else:
            z1.append(zi)
            zlabels.append(yi)

    clf = svm.LinearSVC()
    clf.fit(z1, zlabels)
    return clf.predict(z2),zOrigRows

#### Get Sign of zi

#######################
### Initializing RH ###
#######################


z1=[]
for i in range(0,len(data),1):
    z1.append([])

for i in range(0,rows,1):
    data[i].append(1)
cols = len(data[0]);

for i in range(0,10000,1):
    w=[]
    w=getRandomW(cols);
    #Finding Projection
    dpList = []
    for j in range(0,rows,1):
        dp=signOfDotProduct(data[j],w)
        #dpList.append(dp)
        #if (trainingLabels.get(i) == None):
        z1[j].append(dp)

### Running Hinge Loss



#############################
### Predicting on Original ###
##############################

originalPreds,originalLabels=ScikitSVM(data,trainingLabels)
file1 = open("predictions_Original_RH.txt", "w")
for i in range(len(originalPreds)):
    pl=int(originalPreds[i])
    if(pl==-1):
        print(0,originalLabels[i], file=file1)
    else:
        print(1, originalLabels[i], file=file1)

##############################
### Predicting on Original ###
##############################


changedPreds,zTransformedLabels=ScikitSVM(z1,trainingLabels)
file2 = open("predictions_Transformed_RH", "w")
for i in range(len(changedPreds)):
    pl = int(changedPreds[i])
    if (pl == -1):
        print(0,zTransformedLabels[i], file=file2)
    else:
        print(1, zTransformedLabels[i], file=file2)

