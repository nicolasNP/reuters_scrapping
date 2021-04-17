#!/usr/bin/env python
# coding: utf-8

# In[126]:


import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

hrefs_list = ['https://www.reuters.com/companies/GOOG.OQ', 
              'https://www.reuters.com/companies/AMZN.OQ', 
              'https://www.reuters.com/companies/AAPL.OQ']
records = []
tab_list = []
i = 0

r = requests.get(hrefs_list[0])
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('button', attrs={'class': 'Tabs-button-1Z4q3'})
for result in results[:-1]:
    tab_name = results[i].find('p').contents[0].lower().replace(' ', '-')
    i += 1
    tab_list.append(tab_name)

for href in hrefs_list:
    
    capital_tab = '{}/{}'.format(href, tab_list[6])
    people_tab = '{}/{}'.format(href, tab_list[4])
    
    r = requests.get(capital_tab)
    soup = BeautifulSoup(r.text, 'html.parser')
    name = soup.find('h1').contents[0]
    capital = int(float(soup.find(text = re.compile('Market Capitalization')).parent.parent.parent.span.contents[0].replace(',','')))
    
    r = requests.get(people_tab)
    soup = BeautifulSoup(r.text, 'html.parser')
    ceo = soup.find(text = re.compile('Chief Executive Officer')).parent.parent.find('span').contents[0]
    
    records.append((name, capital, ceo))


# In[127]:


dataframe_reuters = pd.DataFrame(records, columns=['Nom', 'Capital (Milliers de $)', 'CEO'])
dataframe_reuters.to_csv('TD_Reuters.csv', index = False, encoding = 'utf-8')
dataframe_reuters


# In[ ]:




