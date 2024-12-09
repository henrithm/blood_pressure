import sqlite3
from datetime import datetime
from flask import Flask, request, render_template_string

app = Flask(__name__)

def init_db():
    """
    initialize sqlite database and tables
    """
    conn = sqlite3.connect('data.db')   #connect to the db file
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS blood_pressure (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            high_pressure INTEGER,
            low_pressure INTEGER,
            result TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')
    conn.commit()   #save changes to the db
    conn.close()    #close the connection to the db

def check_hypertension(high, low):
    """
    see if is hypertension
    """
    if high >= 140 or low >= 90:
        return "High Blood Pressure"
    else:
        return "Normal"

@app.route('/')
def home():
    """
    show a dynamically generated form page, and display the history records
    """
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT high_pressure, low_pressure, result, timestamp FROM blood_pressure")
    records = cursor.fetchall() #get all records form the db
    conn.close()    #close the connection

#convert the records into the html for display
    records_html = ""
    for record in records:
        records_html += f"""
            <p>High Pressure: {record[0]}, Low Pressure: {record[1]}, Result: {record[2]}, Timestamp:{record[3]}</p>
        """

#generate the html page
    html_code = f'''
    <h1>Check Blood Pressure</h1>
    <form action="/submit" method="post">
        <label>High Pressure:</label>
        <input type="number" name="high_pressure" required><br><br>
        <label>Low Pressure:</label>
        <input type="number" name="low_pressure" required><br><br>
        <button type="submit">Submit</button>
    </form>
    <hr>
    <h2>History Records</h2>
    {records_html}
    '''
    return render_template_string(html_code)

@app.route('/submit', methods=['POST'])
def submit():
    """
    accept user's information about blood pressure, judge whether it is hypertension or normal, and restore it to the db
    """
    #get user inputs from the form
    high = int(request.form['high_pressure'])
    low = int(request.form['low_pressure'])
    result = check_hypertension(high, low)  #evaluate the blood pressure
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')    #get the current time

#save the submitted data to the db
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO blood_pressure (high_pressure, low_pressure, result, timestamp)
        VALUES (?, ?, ?, ?)
        ''', (high, low, result, timestamp))
    conn.commit()
    conn.close()

#show the result page
    result_page = f'''
    <h1>Blood Pressure Result</h1>
    <p>High Pressure: {high}</p>
    <p>Low Pressure: {low}</p>
    <p>Result: {result}</p>
    <p>Timestamp: {timestamp}</p>
    <a href="/">Go Back</a>
    '''
    return render_template_string(result_page)

if __name__ == '__main__':
    init_db()   #perpare the db
    app.run(debug=True) #start the server

