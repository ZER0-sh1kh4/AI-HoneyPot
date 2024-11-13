from flask import Flask,request,jsonify, render_template
import pandas as pd
import json
app = Flask(__name__)
@app.route('/')
def index():
    df = pd.read_json('/home/kali/cowrie/var/log/cowrie/cowrie.json')
    data = df.to_html()
    return render_template('index.html', data=data)
@app.route('/analyze', methods=['POST'])
def analyze():
    log_entry = request.json.get('log')
    if log_entry:
        # Parse log entry into JSON (assuming it’s passed as a JSON-formatted string)
        try:
            log_data = json.loads(log_entry)
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid log format. Ensure it's properly formatted JSON."}), 400

        # Example: Basic analysis based on event type
        if log_data.get("eventid") == "cowrie.login.failed":
            analysis_result = (
                f"Failed login attempt detected for user '{log_data.get('username')}' "
                f"with password '{log_data.get('password')}'. "
                "This could indicate a brute force or credential stuffing attempt."
            )
        elif log_data.get("eventid") == "cowrie.session.connect":
            analysis_result = (
                f"New session started from IP {log_data.get('src_ip')} to destination IP {log_data.get('dst_ip')}. "
                "Monitoring recommended to detect unusual activity."
            )
        else:
            analysis_result = "Log entry recorded, but no specific analysis available."

        return jsonify({"result": analysis_result})
    else:
        return jsonify({"error": "No log entry provided"}), 400
       
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

