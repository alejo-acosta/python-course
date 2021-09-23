#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
# plt.style.use('seaborn')
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Computer Modern"]})
plt.clf()
get_ipython().run_line_magic('matplotlib', 'inline')

import plotly.io as pio
import plotly.express as px
import plotly.offline as py
import plotly.graph_objects as go


# In[2]:


delta = 0.025
x = np.arange(1, 10, delta)
y = np.arange(1, 10, delta)

X, Y = np.meshgrid(x, y)
Z = X**0.5 * Y**0.5


# In[3]:


fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z, 20)
ax.set_aspect('equal', adjustable='box')
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Lineas de contorno')


# In[4]:


fig = go.Figure(data=[go.Surface(z=Z)])
fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                  highlightcolor="limegreen", project_z=True))
fig.update_layout(title='Mt Bruno Elevation', autosize=False,
                  scene_camera_eye=dict(x=1.87, y=0.88, z=-0.64),
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90)
)
fig.show()

