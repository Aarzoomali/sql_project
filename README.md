# Housing & Sentiment Signals: Price Trends Meet Public Opinion

## 🔧 Tech Stack

- Python
- SQL
- PostgreSQL on AWS RDS
- GitHub Actions
- Jupyter Notebooks
- Looker Studio
- draw.io (for diagrams)

---

## 🎯 Project Objective

**Who am I helping?**  
Housing analysts, real estate firms, and market researchers

**What problem am I solving?**  
Fragmented understanding of housing price trends and public sentiment

**How am I solving it?**  
By combining structured housing price data from Zillow with unstructured user sentiment from Reddit to generate actionable insights

---

## 🏢 Job Description

This project was designed to align with a **Data Analytics Intern** position at **First American Financial Corporation**, which emphasized SQL, data visualization, and communication skills.  
The job involved supporting business stakeholders using analytical tools and databases to derive insights related to real estate.

📄 [View Job Description](./proposal/Job%20Description.pdf)

---

## 📊 Data Sources

### 1. Zillow API (Structured Data)
- Source: [Zillow API via RapidAPI](https://rapidapi.com)
- Data: City-level median listing prices
- Relevance: Reflects housing trends and pricing insights

### 2. Reddit Web Scrape (Unstructured Data)
- Source: [r/RealEstate Subreddit](https://www.reddit.com/r/RealEstate/)
- Method: Web scraping using `requests` and `BeautifulSoup`
- Data: User-generated housing sentiment via post titles
- Relevance: Captures public discourse on buying/selling behavior

---

## 📁 Notebooks & Scripts

| File                                                  | Purpose                                      |
|-------------------------------------------------------|----------------------------------------------|
| `notebooks/zillow_API_Extract_Load_Raw.ipynb`         | Pulls and loads Zillow API data              |
| `notebooks/zillow_API_SQL_Analysis.ipynb`             | Performs SQL analysis on price trends        |
| `notebooks/reddit_Web_Scrape_Extract_Load_Raw.ipynb`  | Scrapes post titles from Reddit              |
| `notebooks/reddit_Web_Scrape_SQL_Analysis.ipynb`      | Analyzes buy/sell patterns from scraped data |

---

## 📌 Diagrams

| File                                                  | Purpose                                   |
|-------------------------------------------------------|-------------------------------------------|
| `data/Zillow_API_Data_Pipeline.pdf`                   | Zillow pipeline: from API to DB           |
| `data/Reddit_Web_Scrape_Data_Pipeline.drawio (2).pdf` | Reddit pipeline: from web scrape to DB    |
| `data/ERD_Zillow.pdf`                                 | Zillow ERD (star schema)                  |
| `data/Reddit_erd.pdf`                                 | Reddit ERD (simplified dimensional model) |

---

## 📈 Dashboards & Visualizations

🔗 **Visualizations were created in Looker Studio** using CSV exports from SQL query results.  
Each data source has two visualizations: one descriptive and one diagnostic.

📄 [View Visualizations](./reports/Visualizations.pdf)

---

## 🧠 Future Improvements

- Use NLP to perform sentiment scoring on Reddit post content
- Add more Zillow metrics (e.g., rent estimates, forecast prices)
- Automate scraping with time-based cron jobs via GitHub Actions

---

## 💼 Proposal & Pitch Deck

📄 [Project Proposal](./proposal/Project%20Proposal.pdf)  
📄 [Presentation Slides](./reports/Presentation.pdf)
