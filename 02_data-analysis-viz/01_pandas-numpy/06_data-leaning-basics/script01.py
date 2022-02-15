#%%
import numpy as np
import pandas as pd
#%%
# laptops = pd.read_csv('laptops.csv')  # error
# print(laptops) # error

laptops = pd.read_csv('laptops.csv', encoding='Latin-1')
# print(laptops.info())
#%%
