
# coding: utf-8

# In[163]:

import pandas as pd
import warnings
from dateutil.parser import parse
warnings.filterwarnings('ignore')


# ### Load the buildings and cpq data

# In[164]:

PATH = 'data/'

cpq = pd.read_csv(PATH + 'ZayoHackathonData_CPQs.csv')
buildings = pd.read_csv(PATH + 'ZayoHackathonData_Buildings.csv')


# ### Remove rows where Account ID, Product Group and Building ID is repeated - except the row where a said Account ID, Product Group and Building ID occurs

# In[165]:

cpq['CreatedDate'] = cpq['CreatedDate'].apply(lambda x : parse(x))
cpq.sort_values(by='CreatedDate', inplace=True)
cpq.drop_duplicates(['Account ID', 'Product Group', 'Building ID'], inplace=True)


# ### Get the count of records by the attribute 'On Zayo Network Status'

# In[166]:

cpq['On Zayo Network Status'].value_counts()


# In[167]:

cpq.columns


# ### Merge the cpq and buildings by doing an inner join

# In[168]:

cpq_business = pd.merge(cpq, buildings, how='inner')


# In[169]:

cpq_business.head()


# In[170]:

len(cpq.loc[cpq['Building ID'] == 'Bldg-108671']), len(cpq_business.loc[cpq_business['Building ID'] == 'Bldg-108671'])


# In[171]:

cpq_business['Building ID'] = cpq_business['Building ID'].apply(str)
cpq_business['Building ID'].unique()


# ### Select only those records that are not on Zayo Network

# In[172]:

cpq_status = cpq_business.loc[cpq_business['On Zayo Network Status'] == 'Not on Zayo Network']


# In[173]:

cpq_status.rename(columns={' X36 MRC List ': 'X36 MRC', ' X36 NRR List ': 'X36 NRR', ' X36 NPV List ': 'X36 NPV'}, inplace=True)


# ### Get price in numbers

# In[174]:

cpq_status['X36 MRC'] = cpq_status['X36 MRC'].replace('[\$,)]','',regex=True).astype(float)
cpq_status['X36 NRR'] = cpq_status['X36 NRR'].str.replace(r'[$,]', '')
cpq_status['X36 NRR'] = cpq_status['X36 NRR'].str.replace('-', '0')
cpq_status['X36 NPV'] = cpq_status['X36 NPV'].str.replace(r'[$,]', '')
cpq_status['X36 NPV'] = cpq_status['X36 NPV'].str.replace('-', '0')
cpq_status[['X36 NRR','X36 NPV']] = cpq_status[['X36 NRR','X36 NPV']].apply(pd.to_numeric)
cpq_status[' Estimated Build Cost '] = cpq_status[' Estimated Build Cost '].replace('[\$,)]','',regex=True).astype(float)
cpq_status.head()


# In[175]:

len(cpq_status['Building ID'].unique())


# ### Filter out the records based on the state

# In[176]:

cpq_CO = cpq_status.loc[cpq_status['State'] == 'CO']
cpq_TX = cpq_status.loc[cpq_status['State'] == 'TX']
cpq_GA = cpq_status.loc[cpq_status['State'] == 'GA']


# ### For each individual state, calculate the profit incurred by each building

# In[177]:

CO_profit = cpq_CO.groupby(cpq_CO['Building ID'])['X36 NPV'].sum().reset_index()
CO_profit.sort_values(by='Building ID', inplace=True)
TX_profit = cpq_TX.groupby(cpq_TX['Building ID'])['X36 NPV'].sum().reset_index()
TX_profit.sort_values(by='Building ID', inplace=True)
GA_profit = cpq_GA.groupby(cpq_GA['Building ID'])['X36 NPV'].sum().reset_index()
GA_profit.sort_values(by='Building ID', inplace=True)


# ### For each building, get the total number of accounts associated with the building

# In[178]:

CO_accounts = cpq_CO.groupby(cpq_CO['Building ID'])['Account ID'].count().reset_index()
CO_accounts.sort_values(by='Building ID', inplace=True)
TX_accounts = cpq_TX.groupby(cpq_TX['Building ID'])['Account ID'].count().reset_index()
TX_accounts.sort_values(by='Building ID', inplace=True)
GA_accounts = cpq_GA.groupby(cpq_GA['Building ID'])['Account ID'].count().reset_index()
GA_accounts.sort_values(by='Building ID', inplace=True)


# In[179]:

CO_accounts.head()


# ### Get the estimated build cost for each state

# In[180]:

build_cost_CO = cpq_CO.groupby(['Building ID',' Estimated Build Cost ']).size().reset_index().rename(columns={0:'count'})
build_cost_TX = cpq_TX.groupby(['Building ID',' Estimated Build Cost ']).size().reset_index().rename(columns={0:'count'})
build_cost_GA = cpq_GA.groupby(['Building ID',' Estimated Build Cost ']).size().reset_index().rename(columns={0:'count'})


# ### Total profit = Profit incurred by each building - Estimated build cost

# In[181]:

CO_profit['Estimated Build Cost'] = build_cost_CO[' Estimated Build Cost ']
CO_profit['Profit Including Build Cost'] = CO_profit['X36 NPV'] - CO_profit['Estimated Build Cost']
CO_profit['Number of Accounts'] = CO_accounts['Account ID']


# In[182]:

TX_profit['Estimated Build Cost'] = build_cost_TX[' Estimated Build Cost ']
TX_profit['Profit Including Build Cost'] = TX_profit['X36 NPV'] - TX_profit['Estimated Build Cost']
TX_profit['Number of Accounts'] = TX_accounts['Account ID']


# In[183]:

GA_profit['Estimated Build Cost'] = build_cost_GA[' Estimated Build Cost ']
GA_profit['Profit Including Build Cost'] = GA_profit['X36 NPV'] - GA_profit['Estimated Build Cost']
GA_profit['Number of Accounts'] = GA_accounts['Account ID']


# In[184]:

CO_profit.sort_values(by='Profit Including Build Cost', ascending=False, inplace=True)
TX_profit.sort_values(by='Profit Including Build Cost', ascending=False, inplace=True)
GA_profit.sort_values(by='Profit Including Build Cost', ascending=False, inplace=True)


# In[185]:

CO_profit.head()


# In[186]:

TX_profit.head()


# In[187]:

GA_profit.head()


# ### Merge the profits dataframe with the original datafrae

# In[188]:

co_buildings_latlong = pd.merge(CO_profit, cpq_status, on='Building ID', how='inner')
tx_buildings_latlong = pd.merge(TX_profit, cpq_status, on='Building ID', how='inner')
ga_buildings_latlong = pd.merge(GA_profit, cpq_status, on='Building ID', how='inner')


# In[189]:

co_buildings_latlong.head()


# ### Generate the profits csv by combining the state dataframes. This csv would be used to generate the data table for the first visualization

# In[190]:

co_buildings_latlong = co_buildings_latlong[['Building ID', 'X36 NPV_x', 'Estimated Build Cost', 'Profit Including Build Cost',
                                            'Latitude', 'Longitude', 'State', 'Number of Accounts', 'Street Address',
                                            'Postal Code', 'Net Classification', 'Type']]
co_buildings_latlong.drop_duplicates(['Building ID'], inplace=True)
tx_buildings_latlong = tx_buildings_latlong[['Building ID', 'X36 NPV_x', 'Estimated Build Cost', 'Profit Including Build Cost',
                                            'Latitude', 'Longitude', 'State', 'Number of Accounts', 'Street Address',
                                            'Postal Code', 'Net Classification', 'Type']]
tx_buildings_latlong.drop_duplicates(['Building ID'], inplace=True)
ga_buildings_latlong = ga_buildings_latlong[['Building ID', 'X36 NPV_x', 'Estimated Build Cost', 'Profit Including Build Cost',
                                            'Latitude', 'Longitude', 'State', 'Number of Accounts', 'Street Address',
                                            'Postal Code', 'Net Classification', 'Type']]
ga_buildings_latlong.drop_duplicates(['Building ID'], inplace=True)


# In[191]:

profits = pd.concat([co_buildings_latlong, tx_buildings_latlong, ga_buildings_latlong])


# In[192]:

profits.to_csv('processedData/profits.csv')


# ### Identify the total number of buildings for each state and write that to a csv

# In[193]:

co_sum = CO_profit['Profit Including Build Cost'].sum()
buildings_co = len(CO_profit)


# In[194]:

tx_sum = TX_profit['Profit Including Build Cost'].sum()
buildings_tx = len(TX_profit)


# In[195]:

ga_sum = GA_profit['Profit Including Build Cost'].sum()
buildings_ga = len(GA_profit)


# In[196]:

import csv
vals = [['CO', co_sum, buildings_co], ['TX', tx_sum, buildings_tx], ['GA', ga_sum, buildings_ga]]

with open('processedData/profit_by_state.csv','wb') as f:
    w = csv.writer(f)
    w.writerow(['State','Total Profit', 'Number of Buildings'])
    for v in vals:
        w.writerow(v)


# In[ ]:



