import pandas as pd
df=pd.read_csv('dissdata.csv')
cols=len(df.columns)
rows=len(df)

numatt = df.select_dtypes(include=['number']).columns.tolist()
nomatt = df.select_dtypes(exclude=['number']).columns.tolist()

print('Number of attributes: ',cols)
print('Number of instances: ',rows)
print('Nominal attributes: ',nomatt)
print('Numerical attributes: ',numatt)
df[numatt] = (df[numatt] - df[numatt].min()) / (df[numatt].max() - df[numatt].min())
print('Normalized data:')
print(df)
numatt = df.select_dtypes(include=['number'])

numr = numatt.shape[0]
dissimilarity_matrix = [[0.0 for _ in range(numr)] for _ in range(numr)]

for i in range(numr):
    for j in range(numr):
        if i>=j:
            dissimilarity_matrix[i][j] = round(sum([abs(numatt.iloc[i, k] - numatt.iloc[j, k]) for k in range(len(numatt.columns))]),2)
        else:
            dissimilarity_matrix[i][j] = 0




print('Dissimilarity matrix for numerical attributes:')
for row in dissimilarity_matrix:
    print(row)


nomatt = df.select_dtypes(exclude=['number'])
nomr=nomatt.shape[0]
dissimilarity_matrix = [[0.0 for _ in range(nomr)] for _ in range(nomr)]

for i in range(numr):
    for j in range(numr):
        if i>=j:
            dissimilarity_matrix[i][j] = round(sum([1 if nomatt.iloc[i, k] != nomatt.iloc[j, k] else 0 for k in range(len(nomatt.columns))]),2)
        else:
            dissimilarity_matrix[i][j] = 0
print('Dissimilarity matrix for nominal attributes:')
for row in dissimilarity_matrix:
    print(row)

mixed_att = df
numr = mixed_att.shape[0]
dissimilarity_matrix = [[0.0 for _ in range(numr)] for _ in range(numr)]
for i in range(numr):
    for j in range(numr):
        if i >= j:
            dissimilarity = 0
            for col in mixed_att.columns.tolist():
                if mixed_att[col].dtype == 'object':
                    dissimilarity += 1/cols if mixed_att[col][i] != mixed_att[col][j] else 0/cols
                else:
                    dissimilarity += abs(mixed_att[col][i] - mixed_att[col][j])
            dissimilarity_matrix[i][j] = round(dissimilarity/cols,2)
        else:
            dissimilarity_matrix[i][j] = 0

print('Dissimilarity matrix for mixed attributes:')
for row in dissimilarity_matrix:
    print(row)


