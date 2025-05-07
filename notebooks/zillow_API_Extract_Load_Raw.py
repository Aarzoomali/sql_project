#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv


# In[3]:


import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')


# In[10]:


print("DB_HOST:", DB_HOST)
print("DB_PORT:", DB_PORT)
print("DB_NAME:", DB_NAME)
print("DB_USER:", DB_USER)
print("DB_PASS:", DB_PASS)


# In[12]:


load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')


# In[13]:


print("DB_HOST:", DB_HOST)
print("DB_PORT:", DB_PORT)
print("DB_NAME:", DB_NAME)
print("DB_USER:", DB_USER)
print("DB_PASS:", DB_PASS)


# In[20]:


import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

# Load DB credentials from .env
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

# Connect to MySQL on AWS
engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Simulated Zillow data
data = {
    'city': ['Los Angeles', 'Austin', 'Miami', 'Denver', 'Seattle'],
    'median_price': [880000, 540000, 600000, 510000, 720000],
    'inventory': [1245, 987, 843, 1021, 1150],
    'date': ['2024-04-01'] * 5
}

df = pd.DataFrame(data)

# Upload to AWS RDS
df.to_sql('zillow_raw', con=engine, schema='sql_project', if_exists='replace', index=False)
print("✅ Zillow data uploaded to AWS.")

