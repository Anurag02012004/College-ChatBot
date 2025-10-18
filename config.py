# Configuration file for College Chatbot

# Flask Configuration
FLASK_HOST = "0.0.0.0"
FLASK_PORT = 5000
FLASK_DEBUG = True

# Chatbot Configuration
MODEL_NAME = "all-MiniLM-L6-v2"  # Sentence Transformer model
TOP_K_RESULTS = 3  # Number of similar documents to retrieve
MIN_SIMILARITY = 0.2  # Minimum similarity threshold

# Data Files
COLLEGE_DATA_FILE = "college_data.json"
LIVE_DATA_FILE = "college_data_live.json"

# Web Scraping
SCRAPE_TIMEOUT = 10  # seconds
UPDATE_INTERVAL = 3600  # Update data every hour (in seconds)

# College Website
COLLEGE_BASE_URL = "https://iiitkalyani.ac.in"
