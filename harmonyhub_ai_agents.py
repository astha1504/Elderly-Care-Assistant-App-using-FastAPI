import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')

if not API_KEY:
    raise ValueError("API Key not found. Please set it in the .env file.")

# Function to create a directory if it doesn't exist
def create_directory(directory_path):
    try:
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            print(f"Directory created: {directory_path}")
        else:
            print(f"Directory already exists: {directory_path}")
    except Exception as e:
        print(f"Error creating directory: {e}")

# Example usage of create_directory
create_directory('some_directory')

# Function that interacts with API
def fetch_data(api_url):
    try:
        response = requests.get(api_url, headers={'Authorization': f'Bearer {API_KEY}'})
        response.raise_for_status()  # Raises an error for bad responses
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Log HTTP errors
    except Exception as err:
        print(f'Other error occurred: {err}')  # Log any other errors

