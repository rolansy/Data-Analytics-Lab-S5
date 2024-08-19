import pandas as pd
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

alpha = 0.05 
if p < alpha:
    conclusion = "There is a significant association between 'a' and 'b'."
else:
    conclusion = "There is no significant association between 'a' and 'b'."

print('Conclusion:', conclusion)