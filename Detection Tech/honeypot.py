import os
import random
import logging
import time
import hashlib
from http.server import SimpleHTTPRequestHandler, HTTPServer
import threading
import pandas as pd
from sklearn.ensemble import IsolationForest
import numpy as np

# Configure logging
logging.basicConfig(filename='honeypot.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def generate_fake_credentials():
    usernames = ['admin', 'user', 'root', 'guest']
    passwords = ['password123', '123456', 'admin123', 'letmein']
    return {
        'username': random.choice(usernames),
        'password': hashlib.md5(random.choice(passwords).encode()).hexdigest()
    }

# Create fake files for deception
def create_decoy_files(directory='decoys'):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for i in range(5):
        filename = f"confidential_{i}.txt"
        filepath = os.path.join(directory, filename)
        with open(filepath, 'w') as f:
            f.write(f"Sensitive Information: {generate_fake_credentials()}")
        logging.info(f"Decoy file created: {filepath}")

# Simple Honeypot Web Server to log unauthorized access
class HoneypotHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        logging.info(f"Unauthorized access attempt detected: {self.client_address}")
        self.send_response(403)
        self.end_headers()
        self.wfile.write(b"Access Denied")

def start_honeypot_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, HoneypotHTTPRequestHandler)
    logging.info(f"Honeypot server running on port {port}")
    httpd.serve_forever()

# Machine Learning Model to Detect Anomalous Behavior
def train_intrusion_detection_model(log_file='honeypot.log'):
    data = []
    with open(log_file, 'r') as f:
        for line in f.readlines():
            timestamp = time.mktime(time.strptime(line.split(' - ')[0], '%Y-%m-%d %H:%M:%S,%f'))
            data.append([timestamp])
    
    data = np.array(data)
    model = IsolationForest(contamination=0.1)
    model.fit(data)
    return model

# Monitor Log Files for Anomalies
def detect_anomalies(model, log_file='honeypot.log'):
    data = []
    with open(log_file, 'r') as f:
        for line in f.readlines():
            timestamp = time.mktime(time.strptime(line.split(' - ')[0], '%Y-%m-%d %H:%M:%S,%f'))
            data.append([timestamp])
    
    data = np.array(data)
    predictions = model.predict(data)
    anomalies = [i for i, p in enumerate(predictions) if p == -1]
    if anomalies:
        logging.warning(f"Potential Intrusion Detected at lines: {anomalies}")
    else:
        logging.info("No anomalies detected.")

if __name__ == "__main__":
    # Generate decoy files
    create_decoy_files()
    
    # Start honeypot server in a separate thread
    threading.Thread(target=start_honeypot_server, daemon=True).start()
    
    # Train ML model for intrusion detection
    time.sleep(5)  # Wait for logs to accumulate
    model = train_intrusion_detection_model()
    detect_anomalies(model)
