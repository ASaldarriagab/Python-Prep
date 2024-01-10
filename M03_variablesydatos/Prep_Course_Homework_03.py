#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:

a= 1


# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:

type(8.5)



# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:


type (a)


# 4) Crear una variable que contenga tu nombre

# In[2]:

name= "Alejandro Saldarriaga"


# 5) Crear una variable que contenga un número complejo

# In[3]:


z= 1+ 3j


# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:


type(z)


# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:


a="True"
b=True



# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:


print("el tipo de dato de a es",type(a),"y el de b",type(b),"no son lo mismo.")


# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:


a=5+3.5


# 11) Realizar una operación de suma de números complejos

# In[2]:


a= 3j
b= 1+4J
c= a+b


# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:

a=3
b=5+3j
c=a+b



# 13) Realizar una operación de multiplicación

# In[5]:

3*4



# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

a=2**8
print(a)


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:


a=27/4
print(a)


# 16) De la división anterior solamente mostrar la parte entera

# In[9]:


a=27//4
print (a)



# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:

b=27%4
print(a)



# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:


c=a*b+8
print(c)

# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:


a="casa "
b="azul"
c=a+b
print(c)


# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:

"2"==2
"uno es tipo str y el otro int"


# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

int("2")==2



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:

a= float("3.8") #no funciona por tiene una "," en vez de un "."



# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:

a=3
a-=1
print(a)


# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

1<<2 #se cambia de 0001 a 0100 con <



# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:

#"2"+2 son de diferentes tipos por lo que no esta permitido operarlos con "+"
a = int("2")+2 
print(a)
b= "2"+ str(2)
print(b) #es diferente cuando es str 
c= float("2")+float(2)
print(c)

# 26) Realizar una operación válida entre valores de tipo entero y string

a="bo"
print(a*2)
# In[30]:



