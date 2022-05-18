#%%
from cProfile import label
from dis import dis
from turtle import distance
import numpy as np
import pandas as pd

from sklearn.metrics.pairwise import euclidean_distances
from sklearn.cluster import  KMeans

import matplotlib.pyplot as plt


# %%
votes = pd.read_csv('114_congress.csv')
print(votes.head())
print(votes.info())
# %% [markdown]
# ## Exploring Data

# %%
print(votes['party'].value_counts())
# %%
print(votes.columns)
print(votes.loc[:, '00001':].describe().loc[['mean', '50%']].T)
print(votes.loc[:, '00001':].mode())
# %% [markdown]
# ## Distance between Senators

# %%
print(votes.iloc[0, 3:].shape)
print(votes.iloc[0, 3:].values.reshape(1,-1).shape)

# %%
distance = euclidean_distances(votes.iloc[0, 3:].values.reshape(1, -1), votes.iloc[2, 3:].values.reshape(1, -1))
print(distance)
# %% [markdown]
# ## Initial clustering
# %%
kmeans_model = KMeans(n_clusters=2, random_state=1)
senator_distances = kmeans_model.fit_transform(votes.loc[:, '00001':])
print(senator_distances[:10])
# %% [markdown]
# ## Exploring the Clusters
# %%
labels = kmeans_model.labels_
print(pd.crosstab(labels, votes['party']))
# %% [markdown]
# ## Exploring Senators in the wrong cluster
# %%
democratic_outliers = votes[(labels == 1) & (votes['party'] == 'D')].copy()
print(democratic_outliers)
# %% [markdown]
# ## Plotting out the Clusters
# %%
plt.scatter(senator_distances[:, 0], senator_distances[:,1], c=labels, lw=0)
plt.show()
# %% [markdown]
# ## Finding the Most Extreme

# %%
extremism = (senator_distances ** 3).sum(axis=1)
votes['extremism'] = extremism

print(votes.sort_values(by='extremism', ascending=False)['name'].head(10))
# %% [markdown]
# Clustering is a powerful way to explore data and find patterns. Unsupervised learning is very commonly used with large datasets where it isn't obvious how to start with supervised machine learning. In general, it's a good idea to try unsupervised learning to explore a dataset before trying to use supervised learning machine learning models.
# 
# In a future lesson, we'll dive more into the k-means clustering algorithm and build our own from the ground up.
