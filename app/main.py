from fastapi import FastAPI
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Create the FastAPI app
app = FastAPI()

# Get the value of the OPEN_API_KEY variable from the environment
open_api_key = os.getenv("OPEN_API_KEY")

# Set up your API endpoints and other app configuration here
