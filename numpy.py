#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[26]:


a=np.array([1,2,3])
print(a*3)


# In[6]:


lists=[1,23,4]
print(lists*3)


# In[7]:


#Get dimension
a.ndim


# In[27]:


#Get shape(row,column)
a.shape


# In[9]:


#Get shape(row,column)
a.shape


# In[12]:


#Get type
a.dtype


# In[ ]:





# In[11]:


a=np.array([1,2,3],dtype='int16')


# In[13]:


#get size(16=2 bytes,32=4 bytes)
a.itemsize


# In[14]:


#Get totalsize
a.nbytes


# # Acessing / Changing specific elements, rows, columns, etc

# In[28]:


b=np.array([[1,2,3,4,5,6,7],[3,15,17,4,10,1,9]])


# In[39]:


print(b.ndim)
print(b.nbytes)
print(b[1,2])
print(b[0,:])#row
print(b[:,2])#column
print(b[0,2:6:1])#with stepsize
b[1,2]=16
b[:,4]=5
print(b)


# ### 3D example

# In[16]:


c=np.array([[[1,2,3],[4,5,6]],[[9,8,7],[10,0,3]]])
print(c)
print(c.ndim)
print(c.itemsize)
print(c.nbytes)
len(c[0][0])
print(c[0,0:])
print(c[0,0,:])


# ## Intializing different types of arrays

# In[22]:


#All zeros
np.zeros((2,3,2),dtype='int32')


# In[23]:


#All Ones
np.ones((3,3,2))


# In[24]:


#Any other decimal
np.full((2,3),10)


# In[31]:


#Any other number
print(np.full_like(b,5))
np.full(b.shape,6)


# In[50]:


#Random number
print(np.random.rand(2,3))
print(np.random.randint(2,5,size=(2,3)))


# In[56]:


#identity matrix
np.identity(4,dtype='int32')


# In[63]:


#repeat matrix
arr=np.array([[2,3,4]])
arr1=np.repeat(arr,3,axis=0)
print(arr1)


# In[73]:


#practice question
on1=np.ones((5,5),dtype='int32')
on1[1:4,1:4]=np.zeros((3,3),dtype='int32')
on1[2,2]=9
on1


# In[75]:


#copy
b=np.array([1,2,4])
a=b.copy()
b[2]=3
print(a,b)


# ### Mathematics

# In[77]:


a=np.array([1,2,3,4,5])


# In[80]:


print(a-2)
print(a+2)
print(a/2)


# In[81]:


np.sin(a)


# ### Linear Algebra

# In[85]:


a=np.full((2,3),2)
print(a)
b=np.full((3,2),3)
print(b)
print(np.matmul(a,b))


# ### Statistics

# In[87]:


stats=np.array([[1,2,3,4],[4,5,6,7]])
print(stats)


# In[88]:


#minimum
np.min(stats)


# In[91]:


#max
np.max(stats,axis=1)


# In[94]:


#sum
np.sum(stats,axis=1)


# ### Reorganizing Arrays

# In[100]:


before=np.array([[1,2,3,4],[4,5,6,7]])
print(before)

after=before.reshape((2,2,2))
print("\n",after)


# In[102]:


#vertical stacking 
v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])
print(np.vstack([v1,v2,v1]))


# In[103]:


#horizontal stacking
print(np.hstack([v1,v2,v1]))


# In[136]:


# practice question
matrix=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]])
print(matrix)
output1=matrix[2:4,0:2]
print(output)
i=0
j=4
output2=matrix[[0,1,2,3],[1,2,3,4]]
print(output2)
output3=matrix[[0,4,5],3:5]
print(output3)


# In[ ]:




