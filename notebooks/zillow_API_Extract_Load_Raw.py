import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# ✅ Load credentials
load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

# ✅ Create PostgreSQL connection
try:
    engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    print("✅ Connected to PostgreSQL.")
except Exception as e:
    print("❌ Connection error:", e)

# ✅ Simulated Zillow data
data = {
    'city': ['Los Angeles', 'Austin', 'Miami', 'Denver', 'Seattle'],
    'median_price': [880000, 540000, 600000, 510000, 720000],
    'inventory': [1245, 987, 843, 1021, 1150],
    'date': ['2024-04-01'] * 5
}

df = pd.DataFrame(data)
print("📝 Zillow DataFrame preview:")
print(df.head())

# ✅ Upload to PostgreSQL
try:
    df.to_sql('zillow_raw', con=engine, schema='sql_project', if_exists='replace', index=False)
    print("✅ Zillow data uploaded to PostgreSQL.")
except Exception as e:
    print("❌ Error uploading Zillow data:", e)
