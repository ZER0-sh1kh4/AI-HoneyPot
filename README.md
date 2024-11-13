# AI-embedded HoneyPot
## Overview
This project demonstrates an AI-embedded honeypot designed to detect, monitor, and analyze malicious activity in real time. Using Cowrie, an interactive SSH and Telnet honeypot, combined with artificial intelligence, this setup provides deeper insights into attacker behavior, trends, and patterns by analyzing the incoming data and alerting about anomalous activity.
 ## Project Objectives:
1. Capture unauthorized access attempts and mimic a vulnerable system.
2. Use AI to identify and classify patterns in the attack data.
3. Visualize AI-driven insights, providing real-time feedback on potential threats.

## Features
**Cowrie Honeypot:** Emulates SSH and Telnet services to attract attackers, logging all interactions.

**AI Analysis:** Uses machine learning algorithms to detect and categorize attacks based on behavioral analysis.

**Real-Time Alerts:** Implements alerting mechanisms for high-risk activities.

**Data Visualization:** Displays attack trends, types, and origin analysis for easier interpretation and understanding.

 ## Tech Stack
1. **HTML, CSS, JavaScript:** Used to create the frontend interface.

  **HTML:** Structure of the web page.

  **CSS:** Styling for table layout, fonts, colors, etc.

  **JavaScript:** Handles form submission, fetch requests, and dynamic content updates.

  **Bootstrap:** Provides a responsive and styled framework for HTML components (e.g., table, buttons, form).

2. **Flask:** A lightweight web framework for Python to build the backend API and serve the HTML pages.

3. **Pandas:** Used for data manipulation and conversion, specifically for reading the Cowrie log file in JSON format and rendering it as HTML.

4. **JSON:** Formats and transfers data between frontend and backend; used to parse and analyze log entries.

5. **Cowrie Honeypot:** Logs attacker interactions with the honeypot; provides data for AI analysis.

6. **Python:**
   
   **Flask Integration:** Server logic and API endpoint management.
   
   **Data Handling:** Parsing and analyzing log entries from Cowrie.

## Installation
**Prerequisites**
**Kali Linux or Ubuntu:** Ensure that your operating system is set up.
**Python 3.x:** Required for running Cowrie and the AI scripts.
**Cowrie:** Install and configure the Cowrie honeypot.

## Deployment
**Web Server:** Hosted on local or cloud infrastructure, with Flask handling API requests.
