#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:


# ran out of time to calculate TF-IDF for sp4, does not work!


# In[2]:


import dask.bag as db
import jsonpickle


# In[3]:


b = db.read_text(['C:\\Users\\thejo\\Documents\\school\\CSCI8360 Data Practicum\\P0\\handout\\data\\pg36.txt',
                 'C:\\Users\\thejo\\Documents\\school\\CSCI8360 Data Practicum\\P0\\handout\\data\\4300-0.txt',
                'C:\\Users\\thejo\\Documents\\school\\CSCI8360 Data Practicum\\P0\\handout\\data\\pg514.txt',
                'C:\\Users\\thejo\\Documents\\school\\CSCI8360 Data Practicum\\P0\\handout\\data\\pg1497.txt',
                'C:\\Users\\thejo\\Documents\\school\\CSCI8360 Data Practicum\\P0\\handout\\data\\pg3207.txt',
                'C:\\Users\\thejo\\Documents\\school\\CSCI8360 Data Practicum\\P0\\handout\\data\\pg6130.txt',
                'C:\\Users\\thejo\\Documents\\school\\CSCI8360 Data Practicum\\P0\\handout\\data\\pg19033.txt',
                'C:\\Users\\thejo\\Documents\\school\\CSCI8360 Data Practicum\\P0\\handout\\data\\pg42671.txt']).filter(lambda x: len(str(x)) >= 1)


# In[4]:


freqs = b.str.lower().frequencies(sort=True).topk(40, key=1)
out = freqs.compute()


# In[5]:


pickle = jsonpickle.encode(out)
f = open("sp4.json", "w")
f.write(pickle)


# In[ ]:





# In[ ]:




