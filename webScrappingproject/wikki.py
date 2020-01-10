#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
import csv

base_url="https://en.wikipedia.org/"
response = requests.get(base_url + "wiki/2018_in_film")
response.status_code
html_soup = BeautifulSoup(response.content, "lxml")
# In[3]:
response
# In[4]:
wik = html_soup.find("table", {"class":"wikitable"})
# In[5]:
tables = wik
# In[7]:
raw_trs = tables.find_all("tr")
# In[8]:
len(raw_trs)
clean_trs = raw_trs[0:12]
# In[9]:
clean_trs = raw_trs[0:12]
# In[10]:
raw_columns, raw_rows = clean_trs[0], clean_trs[1:]
# In[11]:
columns = [td.text.replace("\n","") for td in raw_columns.find_all("th")]

# In[12]:

columns

# In[13]:
rows = [[td.text.strip().replace("\n","") for td in row.find_all(["th","td"])] for row in raw_rows]
# In[14]:
rows
# In[15]:
def get_dict(**datas):
    columns = datas.get('columns')
    rows = datas.get('rows')
    return [dict(zip(columns, row)) for row in rows]

# In[17]:
datas = get_dict(columns=columns, rows=rows)
# In[18]:
datas
# In[20]:
import csv
def write_to_csv(datas):
    with open('top10highestworldwidegeosscollectionmovies.csv', 'w') as write_file:
        writer = csv.DictWriter(write_file, fieldnames=datas[0].keys())
        writer.writeheader()
        writer.writerows(datas)


# In[21]:
write_to_csv(datas)

# In[24]:

# In[ ]:




