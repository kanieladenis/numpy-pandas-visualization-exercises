#!/usr/bin/env python
# coding: utf-8

# ## 1 Use matplotlib to plot the following equation:
# 
# y = x^2 − x + 2
# You'll need to write the code that generates the x and y points.
# 
# Add an anotation for the point 0, 0, the origin.

# In[2]:


import matplotlib.pyplot as plt


# In[46]:


x = range(-10,10)
y = [x*x -x + 2 for x in x]


# In[35]:


plt.plot(x,y)
plt.annotate('Origin', xy=(0,0), xytext=(0,20), arrowprops=dict(arrowstyle='->'))


# ## 2) Create and label 4 separate charts for the following equations (choose a range for x that makes sense):
# 
# - y=√x
# - y=x^3
# - y=2^x
# - y=1/(x+1)
# 

# In[40]:


import math


# In[50]:


x = range(0,20)
y = list(math.sqrt(n) for n in x)


# In[59]:


plt.plot(x,y,
        label = 'y=√x line',
        linestyle = '--')
plt.title('y=√x chart')
plt.xlabel('x range')
plt.ylabel('y range')


# ### y=x^3

# In[61]:


x = range(0,20)
y = list(n**3 for n in x)
plt.plot(x,y,
        label = 'y=x**3 line',
        linestyle = '--')
plt.title('y=x**3chart')
plt.xlabel('x range')
plt.ylabel('y range')


# ### y=2^x

# In[62]:


x = range(0,20)
y = list(2**n for n in x)
plt.plot(x,y,
        label = 'y=2**n line',
        linestyle = '--')
plt.title('y=2**n chart')
plt.xlabel('x range')
plt.ylabel('y range')


# ### y=1/(x+1)

# In[63]:


x = range(0,20)
y = list(1/(n+1) for n in x)
plt.plot(x,y,
        label = 'y=1/(x+1) line',
        linestyle = '--')
plt.title('y=1/(x+1) chart')
plt.xlabel('x range')
plt.ylabel('y range')


# ## 3) Combine the figures you created in the last step into one large figure with 4 subplots.

# In[64]:


x = range(0,11)
y1 = list(math.sqrt(n) for n in x)
y2 = list(n**3 for n in x)
y3 = list(2**n for n in x)
y4 = list(1/(n+1) for n in x)

plt.subplot(2,2,1)
plt.plot(x,y1)

plt.subplot(2,2,2)
plt.plot(x,y2)

plt.subplot(2,2,3)
plt.plot(x,y3)

plt.subplot(2,2,4)
plt.plot(x,y4)


# ## 4) Combine the figures you created in the last step into one figure where each of the 4 equations has a different color for the points. Be sure to include a legend and an appropriate title for the figure.

# In[77]:


x = range(0,11)
y1 = list(math.sqrt(n) for n in x)
y2 = list(n**3 for n in x)
y3 = list(2**n for n in x)
y4 = list(1/(n+1) for n in x)

plt.figure(figsize=(10,10))
plt.title("4 Function Line")

plt.plot(x,y1,
        label = 'sqrt(n)',
        color = 'b',
        linestyle = '--')


plt.plot(x,y2,
        label = 'n^3',
        color = 'g',
        linestyle = '--')

plt.plot(x,y3,
        label = '2^n',
        color = 'r',
        linestyle = '--')


plt.plot(x,y4,
        label = '1/(n+1)',
        color = 'y',
        linestyle = '--')

plt.legend()
plt.tight_layout()


# In[ ]:


## Make a new Jupyter notebook named big_o_notation.ipynb
- Title your chart "Big O Notation"
- Label your x axis "Elements"
- Label your y axis "Operations"
- Label your curves or make a legend for the curves
- Use LaTex notation where possible


# In[ ]:




