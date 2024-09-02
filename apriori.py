import pandas as pd

df=pd.read_csv('apriori_data.csv')

print(df)
d={}
for r in df:
    l=list(df[r])
    for i in l:
        if i not in d.keys():
            d[i]=1
        else:
            d[i]+=1
n=sum(d.values())
print("\nId\tFreq\tSupport")
for k,v in d.items():
    print(k,v,str(round(((v/n)*100),2))+'%',sep="\t")

