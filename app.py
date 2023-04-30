from flask import Flask, render_template, request, jsonify
import sqlite3
from configparser import ConfigParser

app = Flask(__name__)

# Load config file
config = ConfigParser()
config.read('config.ini')
companiesDetail = []

for section in config.sections():
    name = config.get(section, 'name')
    code = config.get(section, 'code')
    companiesDetail.append({'name': name, 'code': code})

# Connect to the database
conn = sqlite3.connect('finance.db')

# Query the data from the database
cursor = conn.execute('''SELECT DISTINCT company FROM finance;''')
rows = cursor.fetchall()

# Close the connection
conn.close()

actualContain = [x for x in companiesDetail if x['code'] in [i[0] for i in rows]]

# Render front page of the website
@app.route('/')
def index():
    return render_template('index.html', actualContain=actualContain)

# Render about page of the website
@app.route('/about/')
def about():
    return render_template('about.html')

# Render stock-date page of the website
@app.route('/stock-date/')
def stock_date():
    return render_template('stock-date.html')

# Render stock-date-company page of the website
@app.route('/stock-date-company/')
def stock_date_company():
    return render_template('stock-date-company.html', actualContain=actualContain)

# Render stock-company page of the website
@app.route('/stock-company/')
def stock_company():
    return render_template('stock-company.html', actualContain=actualContain)


# Endpoint to get all stock data for a particular day
@app.route('/stock-date/<date>')
#date formate should be like 'Apr 03, 2023'
def get_stock_data_by_date(date):
    # Connect to the database
    conn = sqlite3.connect('finance.db')

    # Query the data from the database
    cursor = conn.execute('''SELECT * FROM finance WHERE date = ?;''', (date,))
    rows = cursor.fetchall() 

    # Close the connection
    conn.close()

    # Convert the data to a JSON response
    data = []
    for row in rows:
        data.append({
            'company': row[0],
            'date': row[1],
            'open': row[2],
            'high': row[3],
            'low': row[4],
            'close': row[5],
            'adj_close': row[6],
            'volume': row[7]
        })
    return jsonify(data)


# Endpoint to get all stock data for a particular company for a particular day
@app.route('/stock-date-company/<company>/<date>')
#company should be like 'IBM' and date shold be like 'Apr 03, 2023'
def get_stock_data_by_company_and_date(company, date):
    # Connect to the database
    conn = sqlite3.connect('finance.db')

    # Query the data from the database
    cursor = conn.execute('''SELECT * FROM finance WHERE company = ? AND date = ?;''', (company, date))
    rows = cursor.fetchall()

    # Close the connection
    conn.close()

    # Convert the data to a JSON response
    data = []
    for row in rows:
        data.append({
            'company': row[0],
            'date': row[1],
            'open': row[2],
            'high': row[3],
            'low': row[4],
            'close': row[5],
            'adj_close': row[6],
            'volume': row[7]
        })
    return jsonify(data)


# Endpoint to get all stock data for a particular company
@app.route("/stock-company/<company>")
#comany name should be like 'IBM'
def get_stock_data_by_company(company):
    # Connect to the database
    conn = sqlite3.connect('finance.db')

    # Query the data from the database
    cursor = conn.execute('''SELECT * FROM finance WHERE company = ?;''', (company,))
    rows = cursor.fetchall()

    # Close the connection
    conn.close()

    # Convert the data to a JSON response
    data = []
    for row in rows:
        data.append({
            'company': row[0],
            'date': row[1],
            'open': row[2],
            'high': row[3],
            'low': row[4],
            'close': row[5],
            'adj_close': row[6],
            'volume': row[7]
        })
    return jsonify(data)


# Endpoint to update stock data for a company by date
@app.route('/stock-update/<company>/<date>', methods=['POST', 'PATCH'])
def update_stock_data_by_company_and_date(company, date):
    # Connect to the database
    conn = sqlite3.connect('finance.db')

    # Parse the request body
    data = request.get_json()

    # Update the data in the database
    conn.execute('''UPDATE finance
                 SET open = ?,
                     high = ?,
                     low = ?,
                     close = ?,
                     adj_close = ?,
                     volume = ?
                 WHERE company = ? AND date = ?;''', (data['open'], data['high'], data['low'], data['close'], data['adj_close'], data['volume'], company, date))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    # Return a success message
    return jsonify({'message': 'Data updated successfully'})


if __name__ == "__main__":
    app.run(debug=True, port=8000)
    #port number is specified at 8000