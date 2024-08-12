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

numatt = df.select_dtypes(include=['number'])

numr = numatt.shape[0]
dissimilarity_matrix = [[0.0 for _ in range(numr)] for _ in range(numr)]

for i in range(numr):
    for j in range(numr):
        if i>=j:
            dissimilarity_matrix[i][j] = sum([abs(numatt.iloc[i, k] - numatt.iloc[j, k]) for k in range(len(numatt.columns))])
        else:
            dissimilarity_matrix[i][j] = 0




# Print the dissimilarity matrix
print('Dissimilarity matrix for numerical attributes:')
for row in dissimilarity_matrix:
    print(row)


nomatt = df.select_dtypes(exclude=['number'])
nomr=nomatt.shape[0]
dissimilarity_matrix = [[0.0 for _ in range(nomr)] for _ in range(nomr)]

for i in range(numr):
    for j in range(numr):
        if i>=j:
            dissimilarity_matrix[i][j] = sum([1 if nomatt.iloc[i, k] != nomatt.iloc[j, k] else 0 for k in range(len(nomatt.columns))])
        else:
            dissimilarity_matrix[i][j] = 0
print('Dissimilarity matrix for nominal attributes:')
for row in dissimilarity_matrix:
    print(row)

mixed_att = df.select_dtypes(include=['number', 'object'])

numr = mixed_att.shape[0]
dissimilarity_matrix = [[0.0 for _ in range(numr)] for _ in range(numr)]

for i in range(numr):
    for j in range(numr):
        if i >= j:
            if mixed_att.iloc[i].dtype == 'object' and mixed_att.iloc[j].dtype == 'object':
                dissimilarity_matrix[i][j] = sum([1 if mixed_att.iloc[i, k] != mixed_att.iloc[j, k] else 0 for k in range(len(mixed_att.columns))])
            else:
                dissimilarity_matrix[i][j] = sum([abs(mixed_att.iloc[i, k] - mixed_att.iloc[j, k]) for k in range(len(mixed_att.columns))])
        else:
            dissimilarity_matrix[i][j] = 0

# Print the dissimilarity matrix
print('Dissimilarity matrix for mixed attributes:')
for row in dissimilarity_matrix:
    print(row)
