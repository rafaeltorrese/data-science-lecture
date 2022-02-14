# %%
import numpy as np
import pandas as pd

# %%
f500 = pd.read_csv('f500.csv')
print(f500.head())
# %%
print(f500.columns)
# %%
print(f500.loc[:, 'company':'revenues'].head())
# %%
fifth_row = f500.iloc[4]
company_value = f500.iloc[0, 0]

# %%
first_column = f500.iloc[:, 0]
print(first_column)
# %%
second_to_sixth_rows = f500.iloc[1:6]
print(second_to_sixth_rows)
# %%[markdown]
# - With `loc[]`, the ending slice is included.
# - With `iloc[]`, the ending slice is not included.
#
#
# %%
first_three_rows = f500.iloc[:3]
first_seventh_row_slice = f500.iloc[[0, 6], :5]
print(first_seventh_row_slice)
# %%
rev_is_null = f500['revenue_change'].isnull()
print(rev_is_null)
# %%
rev_change_null = f500[rev_is_null]
print(rev_change_null[['company', 'country', 'sector']])
# %%[markdown]
# ### Instructions

# - Use the `Series.isnull()` method to select all rows from `f500` that have a null value for the `previous_rank` column. Select only the `company`, `rank`, and `previous_rank` columns. Assign the result to `null_previous_rank`.

#

# %%
print(f500.columns)

# %%
null_previous_rank = f500.loc[f500['previous_rank'].isnull(), [
    'company', 'rank', 'previous_rank']]

print(null_previous_rank)
# %%
print(f500['previous_rank'].isnull().value_counts())
