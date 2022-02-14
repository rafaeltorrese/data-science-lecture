# %%
import numpy as np
import pandas as pd

# %%
f500 = pd.read_csv('f500.csv', index_col=0)
f500.index.name = None
# %%

print()
print(f500.info())
print(f500.columns)
# %%
print(f500['previous_rank'].value_counts())
# %%
f500.loc[f500['previous_rank'] == 0, 'previous_rank'] = np.nan
# %%[markdown]
# ## Pandas Documentation
# [Pandas Read Csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
# %%
f500_selection = f500[['rank', 'revenues', 'revenue_change']].head()
print(f500_selection)
