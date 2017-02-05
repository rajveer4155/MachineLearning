##############################################
##### Author:Rajveer Sidhu              ######
##### Naive Bayes                       ######
##############################################

import sys
###############################
###### Reading Data File#######
###############################
dataFile=sys.argv[1];
f=open(dataFile,'r');
data=[];
i=0;
j=0;
l=f.readline();
while(l!=''):
	a=l.split();
	l2=[]
	for j in range(0,len(a),1):
		l2.append(float(a[j]));
	data.append(l2);
	l=f.readline();
rows=len(data);
cols=len(data[0]);

###############################
###### Reading Label File######
###############################
labelFile=sys.argv[2]
f=open(labelFile,'r');
trainingLabels={};
i=0;
j=0;
count={};
count[0]=0;
count[1]=0;
l=f.readline();
while(l!=''):
	a=l.split();
	trainingLabels[int(a[1])]=a[0]
	if int(a[0])==0:
		count[0]+=1;
	else:
		count[1]+=1;
	l=f.readline();
f.close()
trows=len(trainingLabels);
tcols=len(trainingLabels[0]);

###############################
###### Calculating Mean########
###############################
meanPositive=[]
meanNegative=[]
sdPositive=[]
sdNegative=[]
## Initialiazing with 1 to avoid zero variance
for j in range(0,cols,1):
	meanPositive.append(1);
	meanNegative.append(1);
	sdPositive.append(1);
	sdNegative.append(1);

for i in range(0,cols,1):	
	for j in range(0,rows,1):
		if(trainingLabels.get(j) != None):
			if(int(trainingLabels[j])==0):
				meanNegative[i]=meanNegative[i]+data[j][i]
			else:			
				meanPositive[i]=meanPositive[i]+data[j][i]


j=0
for j in range(0,cols,1):
	meanNegative[j]=meanNegative[j]/count[0];
	meanPositive[j]=meanPositive[j]/count[1];

###############################
###### Calculating S.D ########
###############################

for i in range(0,cols,1):
	for j in range(0,rows,1):
		if(trainingLabels.get(j) != None):
			if(int(trainingLabels[j])==0):
				sdNegative[i]=sdNegative[i]+(data[j][i]-meanNegative[i])**2
			else:			
				sdPositive[i]=sdPositive[i]+(data[j][i]-meanPositive[i])**2
j=0
for j in range(0,cols,1):
	sdNegative[j]=sdNegative[j]/count[0];
	sdPositive[j]=sdPositive[j]/count[1];

############################
######Classify Labels#######
############################
#file = open("predictionLabelsME.txt", "w")
i=0
j=0

for i in range(0,rows,1):
	dPositive=0;
	dNegative=0;
	if(trainingLabels.get(i) == None):
		for j in range (0,cols,1):			
			dNegative=dNegative+(meanNegative[j]-data[i][j])**2 /sdNegative[j];			
			dPositive=dPositive+(meanPositive[j]-data[i][j])**2/sdPositive[j];
	
		if(dNegative < dPositive):
			print("0 " + str(i))
			#file.write("0 "+ str(i)+"\n")
		else:
			print("1 " + str(i))			
			#file.write("1 "+ str(i)+"\n")

















 

