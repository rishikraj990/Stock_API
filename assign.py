import sqlite3    # For database connection
import requests            # For making connection to server
from bs4 import BeautifulSoup   # For data scrappimg
from configparser import ConfigParser           # For using config file

# Define the User Agent
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

# Load config file
config = ConfigParser()
config.read('config.ini')
companies = []              # Used to generate table in website

for section in config.sections():
    name = config.get(section, 'name')
    code = config.get(section, 'code')
    companies.append(code)         # Get the code name of each company to show table
    # Companies contains = ['IBM', 'CSCO', 'INTC', 'ORCL', 'WMT']

# Connect to the SQLite database
conn = sqlite3.connect('finance.db')

# Create a table if not exist to store the finance data
conn.execute('''CREATE TABLE IF NOT EXISTS finance
             (company TEXT,
             date TEXT,
             open FLOAT DEFAULT NULL,
             high FLOAT DEFAULT NULL,
             low FLOAT DEFAULT NULL,
             close FLOAT DEFAULT NULL,
             adj_close FLOAT DEFAULT NULL,
             volume INTEGER DEFAULT NULL,
             PRIMARY KEY (company, date));''')
conn.commit()

# Define the URL for the finance data for a single company
for company in companies:
  url = f'https://finance.yahoo.com/quote/{company}/history?p={company}'

  # Make a GET request to the URL
  response = requests.get(url, headers=headers)

  # Parse the HTML content using BeautifulSoup
  soup = BeautifulSoup(response.content, 'html.parser')

  # Find the table containing the finance data
  table = soup.find('table', {'data-test': 'historical-prices'})

  # Extract the data from the table
  rows = table.find_all('tr')
  data = []
  for row in rows[1:]:
      cols = row.find_all('td')
      cols = [col.text.strip() for col in cols]
      data.append(cols)

  # Insert the data into the database
  for row in data:
    if len(row)==7:
      conn.execute('''INSERT OR IGNORE INTO finance (company, date, open, high, low, close, adj_close, volume)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (company, row[0], row[1], row[2], row[3], row[4], row[5], row[6]))


# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()