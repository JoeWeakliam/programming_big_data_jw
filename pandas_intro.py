
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd


# In[ ]:




# In[2]:

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])


# In[3]:

s


# In[4]:

s.index


# In[5]:

pd.Series(np.random.randn(5))


# In[6]:

d = {'a' : 0., 'b' : 1., 'c' : 2.}


# In[7]:

d


# In[8]:

pd.Series(d)


# In[9]:

pd.Series(d, index=['b', 'c', 'd', 'a'])


# In[10]:

pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])


# In[11]:

s


# In[12]:

s[0]


# In[13]:

s[:3]


# In[14]:

s[s > s.median()]


# In[15]:

s[[4, 3, 1]]


# In[16]:

np.exp(s)


# In[17]:

s['a']


# In[18]:

s['e'] = 12.


# In[19]:

s


# In[20]:

if 'e' in s:
    print s['e']


# In[21]:

s.get('f')


# In[22]:

s.get('e')


# In[23]:

s.get('f', np.nan)


# In[24]:

s + s


# In[25]:

s * 2


# In[26]:

s[1:] + s[:-1]


# In[27]:

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
   'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}


# In[28]:

d


# In[29]:

df = pd.DataFrame(d)


# In[30]:

df


# In[31]:

pd.DataFrame(d, index=['d', 'b', 'a'])


# In[32]:

d = {'one' : [1., 2., 3., 4.],
     'two' : [4., 3., 2., 1.]}


# In[33]:

d


# In[34]:

pd.DataFrame(d)


# In[35]:

pd.DataFrame(d, index=['a', 'b', 'c', 'd'])


# In[36]:

data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])


# In[37]:

data


# In[38]:

data[:] = [(1,2.,'Hello'), (2,3.,"World")]


# In[39]:

data


# In[40]:

pd.DataFrame(data)


# In[41]:

pd.DataFrame(data, index=['first', 'second'])


# In[42]:

pd.DataFrame(data, columns=['C', 'A', 'B'])


# In[43]:

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]


# In[44]:

data2


# In[45]:

pd.DataFrame(data2)


# In[46]:

pd.DataFrame(data2, index=['first', 'second'])


# In[47]:

pd.DataFrame(data2, columns=['a', 'b'])


# In[48]:

df


# In[49]:

df['one']


# In[50]:

df['three'] = df['one'] * df['two']


# In[51]:

df


# In[52]:

df['flag'] = df['one'] > 2


# In[53]:

df


# In[54]:

del df['two']


# In[55]:

df


# In[56]:

three = df.pop('three')


# In[57]:

df


# In[58]:

three


# In[59]:

df['foo'] = 'bar'


# In[60]:

df


# In[61]:

df['one_trunc'] = df['one'][:2]


# In[62]:

df


# In[63]:

df.insert(1, 'bar', df['one'])


# In[64]:

df


# In[ ]:



