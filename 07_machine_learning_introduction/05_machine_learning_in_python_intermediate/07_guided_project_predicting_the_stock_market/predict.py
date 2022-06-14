#%%
from datetime import datetime
#%%
from datetime import timedelta
#%%
import numpy as np
import pandas as pd

# %%
sphist = pd.read_csv('sphist.csv', parse_dates=['Date'])
#%%
print(sphist.head())
print(sphist.dtypes)
#%%

print(sphist.info())
# %%
sphist.sort_values(by='Date', inplace=True, ignore_index=True)
#%%
print(sphist['Date'].head())
#%%
print(sphist.iloc[0:3])
#%%
print(sphist[sphist['Date'] > '1950-12-25']['Close'].rolling(5, closed='left').mean())
#%%
print(sphist['Date'].iloc[0] + timedelta(days=355))
#%%
print(sphist['Date'].loc[16349:16339])
#%%
print(sphist[0])