
import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


# %%
import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

# ✅ Create MySQL connection string using pymysql
engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ✅ Web scraping: Reddit real estate titles
headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://www.reddit.com/r/RealEstate'
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

titles = [tag.get_text() for tag in soup.find_all('h3') if tag.get_text()]
df = pd.DataFrame({'title': titles})

# ✅ Upload to AWS MySQL
df.to_sql('reddit_raw', con=engine, schema='sql_project', if_exists='replace', index=False)
print("✅ Reddit data uploaded to AWS.")



