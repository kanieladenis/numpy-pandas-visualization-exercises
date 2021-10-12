#!/usr/bin/env python
# coding: utf-8

# ## Make a new Jupyter notebook named big_o_notation.ipynb
# - Title your chart "Big O Notation"
# - Label your x axis "Elements"
# - Label your y axis "Operations"
# - Label your curves or make a legend for the curves
# - Use LaTex notation where possible

# In[22]:


import math
import matplotlib.pyplot as plt

x = x = range(1,11)

y1 = list(0*n + 1 for n in x)
y2 = list(math.log(n) for n in x)
y3 = list(n for n in x)
y4 = list(n * math.log(n) for n in x)
y5 = list(n**2 for n in x)
y6 = list(2**n for n in x)
y7 = list(math.factorial(n) for n in x)
y8 = list(n**n for n in x)

plt.plot(x,y1,
        label = 'O(1)',
        color = 'b',
        linestyle = '--')
plt.plot(x,y2,
        label = 'O(log n)',
        color = 'g',
        linestyle = '--')
plt.plot(x,y3,
        label = 'O(n)',
        color = 'r',
        linestyle = '--')
plt.plot(x,y4,
        label = 'O(n log n)',
        color = 'r',
        linestyle = '--')
plt.plot(x,y5,
        label = 'O(n^2)',
        color = 'y',
        linestyle = '--')
plt.plot(x,y6,
        label = 'O(2^n)',
        color = 'c',
        linestyle = '--')
plt.plot(x,y7,
        label = 'O(n!)',
        color = 'm',
        linestyle = '--')
plt.plot(x,y8,
        label = 'O(n^n)',
        color = 'k',
        linestyle = '--')

plt.title('Big O Notation')
plt.xlabel('Elements')
plt.ylabel('Operations')
plt.legend()
plt.tight_layout()
plt.figure(figsize=(10,10))
                  


# ### y=0n+1 and label the curve "O(1)"

# In[11]:


x = range(1,11)
y = list(0*n + 1 for n in x)
plt.plot(x,y)


# ### y=log(n)and label the curve "O(log n)"

# In[12]:


x = range(1,11)
y = list(math.log(n) for n in x)
plt.plot(x,y)


# ### y=n and label the curve "O(n)"

# In[13]:


x = range(1,11)
y = list(n for n in x)
plt.plot(x,y)


# ### y=n∗log(n)and label it "O(n log n)"

# In[14]:


x = range(1,11)
y = list(n * math.log(n) for n in x)
plt.plot(x,y)


# ### y=n^2 and label it "O(n^2)"

# In[15]:


x = range(1,11)
y = list(n**2 for n in x)
plt.plot(x,y)


# ### y=2^n and label it "O(2^n)"

# In[16]:


x = range(1,11)
y = list(2**n for n in x)
plt.plot(x,y)


# ### y=n! and label it "O(n!)"

# In[17]:


x = range(1,11)
y = list(math.factorial(n) for n in x)
plt.plot(x,y)


# ### y=n^n and label it "O(n^n)"

# In[18]:


x = range(1,11)
y = list(n**n for n in x)
plt.plot(x,y)


# In[ ]:




