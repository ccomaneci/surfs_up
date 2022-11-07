#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


#creating flask routes
@app.route('/')
def hello_world():
    return 'Hello world'


# In[5]:




