import pandas as pd
from math import sqrt as m

k=int(input('Enter the number of clusters: '))
df=pd.read_csv('kmeans.csv')

a=list(df.weight)
b=list(df.height)

x1=a[0]
y1=b[0]
cd={}
for i in range (k):
    cd[i]=[(a[i],b[i])]

d={}
for i in range(k,len(a)):
    x2=a[i]
    y2=b[i]
    for y in range(k):
        x1,y1=cd[y][0]
        d[y]=m((x2-x1)**2+(y2-y1)**2)
    min_d=min(d,key=d.get)
    cd[min_d].append((x2,y2))
    d.clear()

for i in range(k):
    print('Cluster',i+1,':',cd[i])
    