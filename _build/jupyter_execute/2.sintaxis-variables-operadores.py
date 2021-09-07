#!/usr/bin/env python
# coding: utf-8

# # 2. Sintaxis, variables y operadores

# ## 2.1. Sintaxis

# En general Python usa una sintaxis en forma de *funciones*: $f(x,y,z)$

# In[1]:


print(1,2, 'hola', 'UDLA')


# Para delimitar texto se puede ocupar doble o simple comillas: "hola" , 'hola'

# Todo lo que esté después del signo numeral # se lee como comentario.

# In[2]:


# Esto es un comentario
print('esto es código. La raíz cuadrada de 2 es = ', 2**0.5) # Esto también es un comentario
# Esta línea también es comentario


# In[3]:


# Algunas funciones específicas se pueden encadenar:

texto = "Investigación"
print(texto.upper().lower())


# In[4]:


# una larga línea de código se puede dividir con backslash \
print("hola"    .upper())


# La sangría son los espacios al comienzo de una línea de código.
# 
# En otros lenguajes de programación la sangría se usa solo por legibilidad (e.g. R, Stata), pero en Python es muy importante.
# 
# Python usa sangría para indicar bloques de código.

# In[5]:


def cubo_mas_uno(x):
    c = x * x * x
    c = c + 1
    return c


# In[6]:


cubo_mas_uno(3)


# ## 2.1. Introducción a datos

# Una variable es una referencia (o vínculo) que hacemos entre un nombre y un espacio en la memoria.

# ### Memory reference

# <p><img alt="UDLA logo" height="480px" src="images/memory.jpg" align="center" hspace="10px" vspace="10px"></p>
# 
# 

# ### Resource allocation

# <p><img alt="UDLA logo" height="480px" src="images/cpu.jpg" align="center" hspace="10px" vspace="10px"></p>

# In[7]:


x = ["a", "b", "c"]

y = x

y[0] = "z"


# In[8]:


# print(x)


# ## Tipos de variables

# ### Numéricas

# In[9]:


enteros = 12345
flotantes = 1.234
complejos = complex(1.2, 3.4)

print(enteros)
print(flotantes)
print(complejos)


# ### String (Texto)

# In[10]:


texto1 = 'Hola Udla'

print(texto1)


# ### Estructurados

# In[ ]:




