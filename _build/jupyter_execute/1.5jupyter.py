#!/usr/bin/env python
# coding: utf-8

# # Jupyter notebooks

# Jupyter Notebooks son una forma bastante interactiva para programar en Python (funciona también en R!).

# ---
# Permite insertar texto y formatearlo:
# - **Negrita**
# - *Cursiva*
# - <font color='red'>Colores</font>
# - <ins> Subrayado </ins>
# 
# También podemos utilizar $\LaTeX$ para escribir fórumulas:
# - $Y = AL^{\alpha}K^{\beta}$
# 
# Finalmente se puede asignar jerarquía para organizar el código de mejor forma:
# 
# ## 1. Librerías
# ## 2. Importar datos
# ### 2.1. Datos crimen
# ### 2.2. Datos UPC
# ## 3. Análisis
# ---

# Todo lo anterior se combina con código, táblas y figuras generadas en Python!

# ## Ejemplo de código, datos y figuras.

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


n = 1000
x = np.random.normal(0,1,n)
y = np.random.normal(0,1,n)
c = np.random.choice([1,2],n)

array = np.array([x,y,c])


# In[3]:


array.shape


# In[4]:


df = pd.DataFrame(array, index=['x','y','c']).T
df.head()


# In[5]:


plt.figure(figsize=(10,10))
plt.scatter(x,y, c=c, cmap='tab10')
plt.show()

