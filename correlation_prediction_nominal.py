import pandas as pd
import numpy as np
df=pd.read_csv('corr_nom.csv')
print(df)
from scipy.stats import chi2_contingency

df = pd.read_csv('corr_nom.csv')

contingency_table = pd.crosstab(df['a'], df['b'])

print(contingency_table)

chi2, p, dof, expected = chi2_contingency(contingency_table)

print('Chi-Square Statistic:', chi2)
print('p-value:', p)
print('Degrees of Freedom:', dof)
print('Expected Frequencies Table:\n', expected)

contingency_table_values=contingency_table.values
n=np.sum(contingency_table_values)
k=min(contingency_table_values.shape)-1
crr=np.sqrt(chi2/(n*k))
print("\nCorrelation : ",crr,"\n")
alpha = 0.05 
if p < alpha:
    conclusion = "There is a significant association between 'a' and 'b'."
else:
    conclusion = "There is no significant association between 'a' and 'b'."

print('Conclusion:', conclusion)