import json
import pandas as pd
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Define paths to the log files
json_log_file_path = os.path.join(os.getcwd(), '/home/kali/cowrie/var/log/cowrie/cowrie.json')  # Corrected path to>
log_file_path = os.path.join(os.getcwd(), '/home/kali/cowrie/var/log/cowrie/cowrie.log')  # Corrected path to log f>

# Load JSON log data from cowrie.json
try:
    with open(json_log_file_path,'r') as f:
        json_logs = json.load(f)
    df_json = pd.DataFrame(json_logs)
    print("JSON logs loaded successfully.")
    print(df_json.head())  # Debug print to show the first few rows of the JSON logs
except FileNotFoundError:
    print(f"Error: {json_log_file_path} not found.")
    df_json = pd.DataFrame()  # Create an empty DataFrame if file is missing

# Load text log data from cowrie.log
try:
    with open(log_file_path, 'r') as f:
        log_lines = f.readlines()
    df_log = pd.DataFrame(log_lines, columns=['log_entry'])
    print("Text logs loaded successfully.")
    print(df_log.head())  # Debug print to show the first few rows of the log file
except FileNotFoundError:
    print(f"Error: {log_file_path} not found.")
    df_log = pd.DataFrame()  # Create an empty DataFrame if file is missing
# Define a route to serve the homepage
@app.route('/')
def home():
    # Print the DataFrame to check if it contains data
    print(f"Dataframe: {df_log}")
    
    # Render the HTML template with log data if available
    if not df_log.empty:
        log_data_html = df_log.to_html(classes="table table-bordered table-striped", index=False)
    else:
        log_data_html = "<p>No log data available.</p>"

    return render_template('index.html', data=log_data_html)
@app.route('/analyze', methods=['POST'])
def analyze_log():
    log_data = request.json.get("log")
    
    if log_data:
        # Define keywords or patterns associated with malicious behavior
        malicious_patterns = [
            "nc -e",  # Reverse shell command
            "curl",  # Malicious downloading
            "wget",  # Malicious downloading
            "sudo",  # Privilege escalation
            "root",  # Attempts to become root
            "chmod",  # Changing file permissions (potential malicious activity)
            "attack",  # Custom keyword to mark anything suspicious
            "bash",  # Shell execution
            "sh",  # Shell execution
            "chmod +x",  # Making a file executable (could indicate a script)
        ]

        # Check for any malicious pattern in the log data
        prediction = "normal"
        for pattern in malicious_patterns:
            if pattern.lower() in log_data.lower():
                prediction = "suspicious"
                break

        # Return result
        response = {
            "result": prediction
        }
        return jsonify(response)
    else:
        return jsonify({"error": "No log data provided"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
