import pandas as pd
df=pd.read_csv('corr_numeric.csv')
am=df.a.mean()
bm=df.b.mean()
n=len(df)
print('Correlation Coefficient: ',round(sum([(df.a[i]-am)*(df.b[i]-bm) for i in range(len(df))])/(len(df)*df.a.std()*df.b.std()),2))
s=0
for i in range(n):
    s+=(df.a[i]-am)*(df.b[i])
asd=df.a.std()
bsd=df.b.std()
print('Covariance Coefficient: ',s/(n*asd*bsd))

print('COvariance : ')
print(df.cov())
print(s/(n-1))

