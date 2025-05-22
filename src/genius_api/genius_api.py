from pathlib import Path
import os
import requests

BASE_URL = "https://api.genius.com"

def get_environment_variables():
    client_secret = os.environ.get("GENIUS_CLIENT_SECRET")
    client_id = os.environ.get("GENIUS_CLIENT_ID")

    if client_secret is None or client_id is None:
        raise ValueError("Please set the GENIUS_CLIENT_SECRET and GENIUS_CLIENT_ID environment variables.")
    return client_secret, client_id

def get_genius_api_key(client_id: str, client_secret: str):
    """
    Get the Genius API key used for authentication.
    """
    response = requests.post(
        f"{BASE_URL}/oauth/token",
        params={
            "client_id": client_id
            "redirect_uri": redirect_uri
        }
    )

