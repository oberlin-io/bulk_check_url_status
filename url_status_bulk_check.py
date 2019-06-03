#!/usr/bin/env python
# coding: utf-8

# In[68]:


import requests as req
from datetime import datetime
import time


# In[57]:


# Paste links column within t
t = """www.example.com
www.example.com/anotherLink"""


# In[58]:


# Get links into a list
links = t.split("\n")


# In[71]:


# Preview links list
for i in links[:5]:
    print(i)

sec = 10
print("Paused for {} seconds.".format(str(sec)))
time.sleep(sec)


# In[60]:


# Get link status code, build CSV for download
csv = ""
for link in links:
    try:
        got = req.get(link)
        csv += link + "," + str(got.status_code) + "\n"
    except:
        csv += link + "," + "JO's script error" + "\n"


# In[61]:


# Preview CSV output
preview = csv.split("\n")
for i in preview[:5]:
    print(i)

print("Paused for {} seconds.".format(str(sec)))
time.sleep(sec)


# In[62]:


# Write out to CSV file (saves to machine)
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H%M")
with open("link_status_" + timestamp + ".csv", "w") as f:
    f.write(csv)


# In[ ]:
