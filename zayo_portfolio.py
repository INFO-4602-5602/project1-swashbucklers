
# coding: utf-8

# In[133]:

import pandas as pd
import json
import warnings
from collections import defaultdict

warnings.filterwarnings('ignore')


# In[134]:

PATH = '../data/'
accounts = pd.read_csv(PATH + 'ZayoHackathonData_Accounts.csv')


# In[135]:

accounts.head()


# In[136]:

accounts[' Total BRR '] = accounts[' Total BRR '].str.replace(r'[$,]', '')
accounts[' Total BRR '] = accounts[' Total BRR '].str.replace('-', '0')
accounts[' Total BRR '] = accounts[' Total BRR '].apply(pd.to_numeric)


# In[137]:

accounts['Industry'] = accounts['Industry'].replace(['^Media/Content$'], ['Media & Content'], regex=True)
accounts['Industry'] = accounts['Industry'].replace(['^Energy$'], ['Energy & Manufacturing'], regex=True)
accounts['Industry'] = accounts['Industry'].replace(['^Manufacturing$'], ['Energy & Manufacturing'], regex=True)


# In[138]:

industry_brr = accounts.groupby(['Industry', 'Vertical'])[' Total BRR '].sum()


# In[139]:

industry_brr = pd.DataFrame(industry_brr).reset_index()


# In[140]:

industry_dict = defaultdict(dict)

for idx, val in industry_brr.iterrows():
    industry_dict[val[0]][val[1]] = val[2]


# In[141]:

with open('../processedData/result.json', 'w') as fp:
    json.dump(industry_dict, fp)


# In[ ]:



