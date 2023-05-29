from flask import Flask, render_template, request
import pyodbc

app = Flask(__name__)

# Database configuration
server = 'your_server'
database = 'your_database'
username = 'your_username'
password = 'your_password'
driver = 'ODBC Driver 17 for SQL Server'

# Create a connection to the SQL Server database
#connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
#conn = pyodbc.connect(connection_string)
#cursor = conn.cursor()

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# Run pipeline route
@app.route('/run-pipeline', methods=['POST'])
def run_pipeline():
    name = request.form['name']
    # Code to run the Synapse pipeline with the provided name
    # ...

    return "Pipeline executed successfully!"

# Execution history route
@app.route('/history')
def history():
    # Fetch execution history from the SQL Server database
    #cursor.execute("SELECT id, executer, job_name, execution_time FROM execution_history ORDER BY id DESC")
    #history = cursor.fetchall()

    return render_template('index.html', history=history)

if __name__ == '__main__':
    app.run()
