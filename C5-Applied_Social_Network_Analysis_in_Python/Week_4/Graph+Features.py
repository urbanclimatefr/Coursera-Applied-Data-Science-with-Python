
# coding: utf-8

# # Creating a feature matrix from a networkx graph
# 
# In this notebook we will look at a few ways to quickly create a feature matrix from a networkx graph.

# In[1]:

import networkx as nx
import pandas as pd

G = nx.read_gpickle('major_us_cities')


# ## Node based features

# In[2]:

G.nodes(data=True)


# In[3]:

# Initialize the dataframe, using the nodes as the index
df = pd.DataFrame(index=G.nodes())


# ### Extracting attributes
# 
# Using `nx.get_node_attributes` it's easy to extract the node attributes in the graph into DataFrame columns.

# In[4]:

df['location'] = pd.Series(nx.get_node_attributes(G, 'location'))
df['population'] = pd.Series(nx.get_node_attributes(G, 'population'))

df.head()


# ### Creating node based features
# 
# Most of the networkx functions related to nodes return a dictionary, which can also easily be added to our dataframe.

# In[5]:

df['clustering'] = pd.Series(nx.clustering(G))
df['degree'] = pd.Series(G.degree())

df


# # Edge based features

# In[6]:

G.edges(data=True)


# In[7]:

# Initialize the dataframe, using the edges as the index
df = pd.DataFrame(index=G.edges())


# ### Extracting attributes
# 
# Using `nx.get_edge_attributes`, it's easy to extract the edge attributes in the graph into DataFrame columns.

# In[8]:

df['weight'] = pd.Series(nx.get_edge_attributes(G, 'weight'))

df


# ### Creating edge based features
# 
# Many of the networkx functions related to edges return a nested data structures. We can extract the relevant data using list comprehension.

# In[9]:

df['preferential attachment'] = [i[2] for i in nx.preferential_attachment(G, df.index)]

df


# In the case where the function expects two nodes to be passed in, we can map the index to a lamda function.

# In[10]:

df['Common Neighbors'] = df.index.map(lambda city: len(list(nx.common_neighbors(G, city[0], city[1]))))

df

