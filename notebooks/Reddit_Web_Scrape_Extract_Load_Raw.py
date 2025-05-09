import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from dotenv import load_dotenv

# ✅ Load credentials from .env
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

# ✅ Web scrape: Reddit titles
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com/',
    'DNT': '1',  # Do Not Track
}

url = 'https://www.reddit.com/r/RealEstate/'
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
titles = [tag.get_text() for tag in soup.find_all('h3') if tag.get_text()]
df = pd.DataFrame({'title': titles})

# ✅ Preview scraped data
if df.empty:
    print("⚠️ No titles scraped. DataFrame is empty.")
else:
    print("✅ Reddit DataFrame preview:")
    print(df.head())

# ✅ Upload to PostgreSQL
try:
    df.to_sql('reddit_raw', con=engine, schema='sql_project', if_exists='replace', index=False)
    print("✅ Reddit data uploaded to PostgreSQL.")
except Exception as e:
    print("❌ Error uploading Reddit data:", e)
