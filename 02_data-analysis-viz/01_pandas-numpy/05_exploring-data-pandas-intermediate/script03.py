# %%
import numpy as np
import pandas as pd
from pprint import pprint
# %%
f500 = pd.read_csv('f500v2.csv')
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
# %%
top5_null_prev_rank = null_previous_rank.iloc[:5]
# %%
previously_ranked = f500[f500['previous_rank'].notnull()]
rank_change = previously_ranked['previous_rank'] - previously_ranked['rank']
print(rank_change.shape)
print(rank_change.tail(3))
# %%
f500['rank_change'] = rank_change
# %%[markdown]
# - boolean arrays are created using any of the Python standard comparison operators: `==` (equal), `>` (greater than), `<` (less than), `!=` (not equal).

# - We combine boolean arrays using boolean operators. In Python, these boolean operators are `and`, `or`, and `not`. In pandas, the operators are slightly different:

# <table>
# <thead>
# <tr>
# <th>pandas</th>
# <th>Python equivalent</th>
# <th>Meaning</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td><code>a &amp; b</code></td>
# <td><code>a and b</code></td>
# <td><code>True</code> if both <code>a</code> and <code>b</code> are <code>True</code>, else <code>False</code></td>
# </tr>
# <tr>
# <td><code>a | b</code></td>
# <td><code>a or b</code></td>
# <td><code>True</code> if either <code>a</code> or <code>b</code> is <code>True</code></td>
# </tr>
# <tr>
# <td><code>~a</code></td>
# <td><code>not a</code></td>
# <td><code>True</code> if <code>a</code> is <code>False</code>, else <code>False</code></td>
# </tr>
# </tbody>
# </table>
# %%
cols = 'company revenues country'.split()
f500_sel = f500[cols].head()
print(f500_sel)
# %%
over_265 = f500_sel['revenues'] > 265_000
china = f500['country'] == 'China'

# We then use the & operator to combine the two boolean arrays using boolean "and" logic
combined = over_265 & china
final_cols = ['company', 'revenues']
result = f500_sel.loc[combined, final_cols]
print(result)
# %%
large_revenue = f500['revenues'] > 100_000
negative_profits = f500['profits'] < 0
combined = large_revenue & negative_profits
big_rev_neg_profit = f500[combined]
print(big_rev_neg_profit)
# %% [markdown]
# ### Part09
# %%
print(sorted(f500['country'].unique()))
# %%
brazil_venezuela = f500[(f500['country'] == 'Brazil')
                        | (f500['country'] == 'Venezuela')]
print(brazil_venezuela)
# %%
print(f500['sector'].unique())
# %%
tech_outside_usa = f500[(f500['sector'] == 'Technology')
                        & (f500['country'] != 'USA')].head()
#%%[markdown]
# ### Part10
#%%[markdown]
# ### Sort values
# 1. Find the company headquartered in Japan with the largest number of employees.
#   - Select only the rows that have a country name equal to Japan.
#   - Use `DataFrame.sort_values()` to sort those rows by the employees column in descending order.
#   - Use `DataFrame.iloc[]` to select the first row from the sorted dataframe.
#   - Extract the `company` name from the index label company from the first row. Assign the result to `top_japanese_employer`.


#%%

top_japanese_employer = f500[f500['country'] == 'Japan'].sort_values('employees',  ascending=False).iloc[0, 0]
print(top_japanese_employer)


#%%[markdown]
# ### Aggregation
#%%
top_employer_by_country = {}
countries = f500['country'].unique()
# print(countries)

for country in countries:
    selected_row = f500[f500['country'] == country].sort_values('employees', ascending=False).iloc[0]
    top_employer_by_country[country] = selected_row['company']

# pprint(top_employer_by_country)

#%%[markdown]
# ### Aggregation challenge
# 
# %%
# pprint(f500.columns)
# step 1
f500['roa'] = f500['profits'] / f500['assets']
# print(f500['profits assets roa'.split()].head())

# step 2
top_roa_by_sector = {}
sectors = f500['sector']
for sector in sectors:
    selected_row = f500[f500['sector'] == sector].sort_values('roa', ascending=False).iloc[0]
    top_roa_by_sector[sector] = selected_row['company']

# pprint(top_roa_by_sector)
#%%
