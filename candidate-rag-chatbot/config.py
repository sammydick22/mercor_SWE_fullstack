import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Weaviate Configuration
WEAVIATE_URL = os.getenv("WEAVIATE_URL", "https://p6ce0pj5rbib30et8ie7ug.c0.us-west3.gcp.weaviate.cloud")
WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY", "HSJEaIn0nUSl3ZOEHmaXd68KryjWAR8CX8vy")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Candidate Collection Configuration
CANDIDATE_COLLECTION = "Candidates"
CANDIDATE_COLLECTION_DESCRIPTION = """
Professional job candidate profiles containing work experience, education history, 
skills, salary expectations, and contact information for hiring purposes.
"""

# Flask Configuration
DEBUG = os.getenv("DEBUG", "False").lower() in ["true", "1", "t"]
PORT = int(os.getenv("PORT", "5000"))
HOST = os.getenv("HOST", "0.0.0.0")
