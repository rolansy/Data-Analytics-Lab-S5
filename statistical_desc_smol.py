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
median=np.median(l)
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
print("Mean : ",np.mean(l))
print("Median : ",np.median(l))
md=list(df.data.mode())
print("Mode : ",end='')
mod={1:'uni',2:'bi',3:'tri'}
for k in md:
        print(k,end=", ")
print('\nThe data has ',mod[len(md)],'mod',sep='')
print("\nVariance : ",np.var(l))
print("Standard Deviation : ",np.std(l))

print('Max : ',max(l))
print('Min : ',min(l))

