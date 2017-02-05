##########################################
### Author: Rajveer Sidhu             ####
### BER for Predicted Labels          ####
##########################################
import os,sys
trueLabels={}
predicitedLabels={}
tn=0; # a
fp=0; # b
fn=0; # c
tp=0; # d

### Reading True Labels ###
trueLabelFile=sys.argv[1];
f1=open(trueLabelFile,'r');

trueLabelsDic={};
i=0;
j=0;

l1=f1.readline();
while(l1!=''):
	a=l1.split();
	trueLabelsDic[int(a[1])]=a[0]
	l1=f1.readline();
f1.close()

### Reading Predicted Labels ###
predLabelFile=sys.argv[2];
f2=open(predLabelFile,'r');

i=0; j=0;
trueLabel=0;
l2=f2.readline();
while(l2!=''):
	b=l2.split();
	if(trueLabelsDic.get(int(b[1])) != None):
		trueLabel=trueLabelsDic.get(int(b[1]));
		if(int(trueLabel)==int(b[0]) and int(trueLabel)==0):
			tn+=1;
		elif(int(trueLabel)==int(b[0]) and int(trueLabel)==1):
			tp+=1;
		elif(int(trueLabel)!=int(b[0]) and int(trueLabel)==1 and int(b[0])==0):
			fn+=1;
		elif(int(trueLabel)!=int(b[0]) and int(trueLabel)==0 and int(b[0])==1):
			fp+=1;
	l2=f2.readline();

print("TP: ", tp, "TN: ", tn,"FN: ", fn, "FP: ", fp);
ber=float(float(fp)/float(tn+fp) + float(fn)/float(tp+fn))*0.5;
print("BER= ", ber);
	
