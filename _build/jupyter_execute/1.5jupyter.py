#!/usr/bin/env python
# coding: utf-8

# # 1.5. Jupyter notebooks

# Jupyter Notebooks son una forma bastante interactiva para programar en Python (funciona también en R!).

# ## 1.5.1. Texto

# ---

# 
# 1. Permite insertar texto y formatearlo:
# - **Negrita**
# - *Cursiva*
# - <font color='red'>Colores</font>
# - <ins> Subrayado </ins>
# 

# 
# 2. Podemos utilizar $\LaTeX$ para escribir fórumulas:
# - $Y = AL^{\alpha}K^{\beta}$
# 

# 3. Asignar jerarquías para mejor organización del código:
# 
# ## 1. Librerías
# ## 2. Importar datos
# ### 2.1. Datos crimen
# ### 2.2. Datos UPC
# ## 3. Análisis

# 4. Finalmente, podemos insertar imágenes:
# <p><img alt="UDLA logo" height="120px" src="https://www.udla.edu.ec/wp-content/uploads/2016/07/Logo.jpg" align="center" hspace="10px" vspace="10px"></p>

# Todo lo anterior se combina con código, tablas y figuras generadas en Python!

# ---

# ## 1.5.2. Ejemplo de código, datos y figuras.

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


n = 1000
c = np.random.choice([1,2],n)
x = np.random.normal(0,1,n) + c*2
y = np.random.normal(0,1,n) + c*1.5

array = np.array([x,y,c])


# In[3]:


array.shape


# In[4]:


df = pd.DataFrame(array, index=['x','y','c']).T
df.head(10)


# In[5]:


fig = plt.figure(figsize=(8,8))
scat = plt.scatter(x,y, c=c, cmap='Accent')
legend1 = plt.legend(*scat.legend_elements(), title="tipos")
plt.show()

