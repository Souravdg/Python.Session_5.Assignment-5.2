#!/usr/bin/env python
# coding: utf-8

# In[10]:


"""
Problem Statement 1:
Implement a Python program to generate all sentences where subject is in
["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
["Baseball","cricket"]
"""

subject=["Americans", "Indians"]
verb=["Play", "watch"]
obj=["Baseball","cricket"]

result = [sub+' '+ver+' '+ob for sub in subject for ver in verb for ob in obj]
for x in range(len(result)):
    print(result[x])

