#!/usr/bin/env python
# coding: utf-8

# # 2. Sintaxis, variables y operadores

# ## 2.1. Sintaxis

# En general Python usa una sintaxis en forma de *funciones*: $f(x,y,z)$

# In[1]:


print(1,2,3, 'hola', 'UDLA')

range(10)


# Python siempre comienza numerando desde **0**, es decir el primer elemento de un arreglo tendrá como índice el número 0. Esta es una característica que Python comparte con la mayoría de lenguajes de programación fuertes (C, Java, Swift, PHP, etc.). El porqué, está fuera del alcance del curso pero si desean entender más sobre este tema, pueden leer el siguiente artículo: [Array Indexing: 0-based or 1-based?](https://medium.com/analytics-vidhya/array-indexing-0-based-or-1-based-dd89d631d11c) o el siguiente ensayo desde una perspectiva matemática: [Why numbering should start at zero](https://www.cs.utexas.edu/users/EWD/ewd08xx/EWD831.PDF).

# Podemos obtener la documentación (*docstring*) de una función utilizando el signo **?** antes de la función:

# In[2]:


get_ipython().run_line_magic('pinfo', 'range')


# Para delimitar texto se puede ocupar doble o simple comillas: "hola" , 'hola'

# Todo lo que esté después del signo numeral # se lee como comentario.

# In[3]:


# Esto es un comentario
print('Esto es código. La raíz cuadrada de 2 es =', 2**0.5) # Esto también es un comentario
# Esta línea también es comentario


# In[4]:


# Algunas funciones específicas se pueden encadenar:

texto = "Investigación"
print(texto.upper().lower())


# In[5]:


# una larga línea de código se puede dividir con backslash \
print("hola"    .upper())


# In[6]:


print('hola'     .       upper())


# La sangría son los espacios al comienzo de una línea de código.
# 
# En otros lenguajes de programación la sangría se usa solo por legibilidad (e.g. R, Stata), pero en Python es muy importante.
# 
# Python usa sangría para indicar bloques de código.

# In[7]:


def cubo_mas_uno(x):
    c = x * x * x
    c = c + 1
    return c


# In[8]:


cubo_mas_uno(3)


# ## 2.1. Introducción a datos

# Una variable es una referencia (o vínculo) que hacemos entre un nombre y un espacio en la memoria.

# ### Memory reference

# <!-- <p><img alt="UDLA logo" height="480px" src="./images/memory.jpg" align="center" hspace="10px" vspace="10px"></p> -->
# ![image](./images/memory.jpg)
# 

# ### Resource allocation

# <!-- <p><img alt="UDLA logo" height="480px" src="./images/cpu.jpg" align="center" hspace="10px" vspace="10px"></p> -->
# ![image](./images/cpu.jpg)

# In[9]:


x = ["a", "b", "c"]

y = x

y[0] = "z"


# In[10]:


print(x)


# ## Tipos de variables

# ### Numéricas

# In[11]:


enteros = 12345
flotantes = 1.234
complejos = complex(1.2, 3.4)

print(enteros)
print(flotantes)
print(complejos)


# ### String (Texto)

# In[12]:


texto1 = 'Hola UDLA'

print(texto1)


# In[13]:


# Multiples líneas de texto
texto_lineas = """
String
en
multiples
líneas
"""

print(texto_lineas)


# In[14]:


# Se puede incluir caracteres especiales con backslash \:
texto_espacio = "línea 1 \n línea 2" # \n = new line
texto_tab = "texto 1 \t texto 2 \t texto3 3" # \t = tabulación

print(texto_espacio)
print("-------------------------")
print(texto_tab)


# ```{admonition} Pregunta
# ¿Por qué "línea 1" y "línea 2" tienen sangrías diferentes?
# ```

# In[15]:


# El texto puede tomar el valor de una variable (formatted text)

numero = 12
texto_formato = f"La raíz de {numero} es {numero**0.5} y su cubo es {numero**3}"

print(texto_formato)


# ### Colecciones de datos (o datos estructurados)

# Son agrupaciones que nos permiten asignar multiples datos a una sola variable.
# 
# Existen 4 tipos de colecciones:

# |                                     | Ordenada |  Indexada  | Modificable | Permite duplicados |
# |:-----------------------------------:|:--------:|:----------:|:-----------:|:------------------:|
# |       **Lista**<br />(*List*)       |     X    |  X (auto)  |      X      |          X         |
# |       **Tupla**<br />(*Tuple*)      |     X    |  X (auto)  |             |          X         |
# | **Diccionario**<br />(*Dictionary*) |     X    | X (manual) |      X      |                    |
# |      **Conjunto**<br />(*Set*)      |          |            |      X      |                    |

# Se declaran de la siguiente manera:

# In[16]:


# LISTAS
list1 = [1, 2, 3, 1, 2, "a", "b", "a", "b"]

# TUPLAS
tuple1 = (1, 2, 3, 4, 5, "a", "b", 1)

# DICCIONARIOS
dict1 = {"ECU": "Ecuador", "COL": "Colombia", "PER": "Perú", "BOL": "Bolivia"}

# SETS
set1 = set(list1)


# In[17]:


print(list1)
print(tuple1)
print(dict1)
print(set1)


# A estas colecciones se les considera estructuras unidemensionales. Sin embargo, podemos representar N dimensiones al anidarlar (*nested lists*).

# In[18]:


matriz = [[3, 4, 5], [2, 6, 7], [0, 1, 9]]
notas = {"A0001": [10, 10, 8, 9, 8], "A0002": [3, 1, 5, 7.4, 8]}

print(matriz)
print(notas)


# La idea es que, al ser un lenguaje **dinámico**, no hay restricción en lo que se puede agrupar en una colección de datos.

# ## Slicing

# Podemos seleccionar datos específicos de las colecciones utilizando el método slicing. **Tener en cuenta que la numeración empieza en 0**.

# In[19]:


list1 = [1, 2, 3, "a", "b", "c"]


# **Lista**
# |key|-key|  Value |
# |---|----|--------|
# | 0 | -6 | 1      |
# | 1 | -5 | 2      |
# | 2 | -4 | 3      |
# | 3 | -3 | a      |
# | 4 | -2 | b      |
# | 5 | -1 | c      |  
#   
#   
# **Diccionario**
# | Key | Value    |
# |-----|----------|
# | ECU | Ecuador  |
# | COL | Colombia |
# | PER | Perú     |
# | BOL | Bolivia  |

# In[20]:


# Seleccionar elementos
print( list1[0] )
print( list1[2] )
print( list1[5] )


# In[21]:


# Seleccionar rangos
print( list1[3:7] )
print( list1[2:] )


# In[22]:


# Seleccionar desde el último elemento
print( list1[-4] )


# In[23]:


# Diccionario
print(dict1["COL"])


# ```{admonition} Pregunta
# En la *lista1* seleccione asigne la letra "z" a los dos elementos interm
# ```

# In[ ]:





# Si las colecciones son modificables (o mutables), podemos modificar datos específicos

# In[24]:


lista2 = [1, 2, 3, "a", "b", "c"]


# ```{admonition} Pregunta
# En la *lista1* seleccione asigne la letra "z" a los dos elementos interm
# ```

# 
# 
