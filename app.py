from flask import Flask, jsonify, request
from datetime import datetime
from flask_cors import CORS  # Import the CORS module
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
print(app)

'''
@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"
'''

# Your existing route for fetching hotels data
@app.route('/api/hotels', methods=['GET'])
def get_hotels():
    conn = sqlite3.connect('hotels.db')
    cursor = conn.cursor()

    # Get the country from the query parameters
    country = request.args.get('country', None)

    if country:
        # If country is provided, filter the results
        cursor.execute('SELECT * FROM hotels WHERE country = ?', (country,))
    else:
        # If country is not provided, get all results
        cursor.execute('SELECT * FROM hotels')

    columns = [col[0] for col in cursor.description]
    hotels = [dict(zip(columns, row)) for row in cursor.fetchall()]

    conn.close()
    return jsonify({'hotels': hotels})

# Route to serve the React app
@app.route('/')
def index():
    return render_template('frontend/build/index.html')

if __name__ == '__main__':
    print(app)
    app.run()
    #createHotelsTable()
