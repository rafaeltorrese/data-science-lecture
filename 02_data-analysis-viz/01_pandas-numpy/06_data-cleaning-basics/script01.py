# %%
import numpy as np
import pandas as pd
# %%
# laptops = pd.read_csv('laptops.csv')  # error
# print(laptops) # error

laptops = pd.read_csv('laptops.csv', encoding='Latin-1')
# print(laptops.info())
# %%
# print(laptops.columns)

#%%

laptops_test = laptops.copy()
laptops_test.columns = 'A B C D E F G H I J K L M'.split()
# print(laptops_test.columns)
#%% [markdown]
# 1. Remove any whitespace from the start and end of each column name.
#      - Create an empty list named `new_columns`.
#      - Use a for loop to iterate through each column name using the `DataFrame.columns` attribute. Inside the body of the for loop:
#          - Use the `str.strip()` method to remove whitespace from the start and end of the string.
#          - Append the updated column name to the `new_columns` list.
#       - Assign the updated column names to the `DataFrame.columns` attribute.

#%%
new_columns = [c.strip() for c in laptops.columns ]
# print(laptops.columns)
# print(new_columns)
laptops.columns = new_columns
# print(laptops.columns)
#%%


