# AI-Deception-Honeypot
AI-driven deception technology using honeypots to detect cyber threats
# AI-Driven Deception Technology

## Overview
This project implements an **AI-driven deception system** for cybersecurity using **honeypots and decoys** to detect and analyze cyber threats. It logs unauthorized access attempts, generates decoy files, and uses machine learning to detect anomalies.

## Features
- **Honeypot Web Server**: Detects unauthorized access attempts.
- **AI-Powered Decoys**: Creates fake files to mislead attackers.
- **Intrusion Detection Model**: Uses machine learning (Isolation Forest) to detect anomalies.
- **Logging & Monitoring**: Records and analyzes attacker behavior.

## Technologies Used
- **Python** (3.9+)
- **Flask** (For web-based honeypots)
- **Machine Learning (Scikit-learn)**
- **Logging & Security Monitoring**
- **Networking (Socket Programming)**

## Installation
### **1. Clone the Repository**
```sh
git clone https://github.com/your-username/AI-Deception-Honeypot.git
cd AI-Deception-Honeypot
```

### **2. Set Up Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4. Run the Honeypot System**
```sh
python honeypot.py
```

## Usage
- The honeypot will **listen on a specified port** and log unauthorized access attempts.
- Decoy files will be generated in the `decoys/` folder.
- The machine learning model will **analyze logs** for potential threats.
- Logs can be monitored in `honeypot.log`.

## Configuration
- **Change the Listening Port**
  - Edit the `start_honeypot_server(port=8080)` function in `honeypot.py`.
- **Modify Decoy File Generation**
  - Adjust `create_decoy_files()` to create different types of fake data.

## Future Enhancements
- **Automated Alert System** (Email/SMS notifications on intrusion detection)
- **Deep Learning Integration** for advanced behavioral analysis.
- **Network-Level Deception** using AI-generated fake network nodes.

## Contributing
1. Fork the repo & clone it locally.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make changes and commit: `git commit -m "Added new feature"`.
4. Push to GitHub: `git push origin feature-branch`.
5. Submit a pull request.

