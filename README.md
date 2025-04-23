# sql_project
# SQL Project – Milestone 1 🚀

## 👋 About the Project
This project is part of a data pipeline milestone where data is extracted from two different sources — an API and a web page — then cleaned and uploaded to an Amazon RDS MySQL database hosted on AWS.

## 📂 Folder Structure

## 🔧 Technologies Used
- **Python**
- **VS Code**
- **Pandas**
- **SQLAlchemy**
- **AWS RDS (MySQL)**
- **Jupyter Notebooks**
- **Requests + BeautifulSoup**

## 📈 What Each Notebook Does
### 1. `zillow_API_Extract_Load_Raw.ipynb`
- Connects to Zillow's API (mock/simulated)
- Extracts housing data
- Loads into a DataFrame
- Uploads to AWS RDS table: `zillow_raw`

### 2. `reddit_Web_Scrape_Extract_Load_Raw.ipynb`
- Scrapes titles from posts on [r/RealEstate](https://www.reddit.com/r/RealEstate/)
- Loads into a DataFrame
- Uploads to AWS RDS table: `reddit_raw`

## 🗄️ Database Details
- **Host**: AWS RDS MySQL instance
- **Schema Name**: `sql_project`
- **Tables Created**:
  - `zillow_raw`
  - `reddit_raw`

## 🙋 Author
- **Name**: Aarzoomali
- **Class**: ISBA 4715
- **Milestone**: 1
- **Date**: April 2025

## 🔒 Note
`.env` file containing credentials is excluded from GitHub for security.

