import pandas as pd
import numpy as np
df=pd.read_csv('statdata.csv')
l=list(df.data)
print(l)
n=len(l)
print("Quartiles : ")
print("Q0 : ",l[0])
q1=l[n//4]
print("Q1 : ",q1)
if n%2==0:
    median=(l[n//2-1]+l[n//2])/2
else:
    median=l[n//2]
print("Q2 : ",median)
q3=l[(n*3)//4]
print("Q3 : ",q3)
print("Q4 : ",l[n-1])
iqr=q3-q1
print("Inter Quartile Range : ",iqr)
ho=q3+(1.5*iqr)
lo=q1-(1.5*iqr)
print('ho: ',ho,'\nlo: ',lo)
print("Low Outliers : ",end='')
p=0
out=[]
for i in range(n//4):
    if l[i]<lo:
        p+=1
        out.append(l[i])
        print(l[i],end=" ")
    else:
        if p==0:
            print('None')
        break
print()
p=0
print("High Outliers : ",end='')
for i in range(n-1,((n*3)//4),-1):
    if l[i]>ho:
        p+=1
        out.append(l[i])
        print(l[i],end=" ")
    else:
        if p==0:
            print('None')
        break
while out:
        l.remove(out.pop())
print()
print(l)
print()
n=len(l)
d={}
for x in l:
	if x not in d.keys():
		d[x]=1
	else:
		d[x]+=1
mean=np.mean(l)
print("Mean : ",mean)
mxx=mkx=0
for k,v in d.items():
	if v>mxx:
		mxx=v
		mkx=k
l.sort()
print("Sorted  : ",l)
if n%2==0:
    median=(l[n//2-1]+l[n//2])/2
else:
    median=l[n//2]
print("Median : ",median)
print("Mode : ",end="")
md=0
mod={1:'uni',2:'bi',3:'tri'}
for k,v in d.items():
    if v==mxx:
        md+=1
        print(k,end=", ")
print('\nThe data has ',mod[md],'mod',sep='')
print("\nVariance : ",np.var(l))
print("Standard Deviation : ",(np.var(l))**(1/2))

print('Max : ',max(l))
print('Min : ',min(l))


