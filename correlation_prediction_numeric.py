import pandas as pd
df=pd.read_csv('corr_numeric.csv')
am=df.a.mean()
bm=df.b.mean()
n=len(df)
s=0
for i in range(n):
    s+=(df.a[i]-am)*(df.b[i]-bm)
asd=df.a.std()
bsd=df.b.std()
corr=s/(n*asd*bsd)
print('Correlation Coefficient: ',corr)
print('Covariance : ',s/(n))
if corr>0:
    print('Positive Correlation')
elif corr<0:
    print('Negative Correlation')
else:
    print('No Correlation')


