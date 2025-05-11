import os
import pandas as pd
import requests
from sqlalchemy import create_engine
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

# ✅ Connect to PostgreSQL
engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
print("✅ Connected to PostgreSQL.")

# ✅ Reddit URL and headers
url = "https://www.reddit.com/r/RealEstate/hot/.json"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept": "application/json"
}

# ✅ Fetch and parse Reddit data
response = requests.get(url, headers=headers)
if response.status_code != 200:
    print(f"❌ Failed to fetch data: {response.status_code}")
    print(response.text)
    exit()

data = response.json()
posts = data["data"]["children"]

# ✅ Extract and clean post titles
titles = [post["data"]["title"].strip() for post in posts]
df = pd.DataFrame(titles, columns=["title"])
print("📝 Reddit DataFrame preview:")
print(df.head())

# ✅ Upload to PostgreSQL
try:
    df.to_sql(
        "reddit_raw",
        con=engine,
        schema="sql_project",
        if_exists="append",
        index=False
    )
    print("✅ Reddit data uploaded to PostgreSQL.")
except Exception as e:
    print("❌ Error uploading Reddit data:", e)

