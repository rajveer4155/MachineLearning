########################################
#### CART Gini Index                ####
#### Author: Rajveer Sidhu          ####
########################################
import sys
import random
import math
from math import exp
from math import log
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
    trainingLabels[int(a[1])] = int(a[0])
    if int(a[0]) == 0:
        count[0] += 1;
    else:
        count[1] += 1;
    l = f.readline();
f.close()

columns = list(zip(*data));


### Defining Function for Dot product START
rowGini={}
colGini={}
sortedCols={}
for j in range(0,cols,1):
    sortedCols[j]=sorted(set(columns[j]));

splitOnColumn = None;
splitValue = 0
gini = float('inf')
for j in range(0,cols,1):
    print(columns[j]);
    print(sortedCols[j]);
    for i in range(len(sortedCols[j])-1):
        avg=(sortedCols[j][i]+sortedCols[j][i+1])/2;
        lsize = float(0);
        rsize = float(0);
        lp = float(0);
        rp = float(0);
        for k in range (rows):
            if(data[k][j]<avg):
                if k in trainingLabels:
                    lsize+=1;
                    if (trainingLabels[k]) == 0:
                        lp += 1;
            else:
                if k in trainingLabels:
                    rsize+=1;
                    if (trainingLabels[k]) == 0:
                        rp += 1;

        gtemp = (lsize / rows) * (lp / lsize) * (1 - lp / lsize) + (rsize / rows) * (rp / rsize) * (1 - rp / rsize);
        if gtemp < gini:
            splitOnColumn = j
            splitValue = avg
            gini = gtemp

print('k =', splitOnColumn)
print('s =', splitValue)
print('gini =', gini)



