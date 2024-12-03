import json
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import re
import random
from cryptography.fernet import Fernet

# Constants
CONFIG_FILE = "config.json"
KEY_FILE = "key.key"

# Generate a key for encryption if it doesn't exist
if not os.path.exists(KEY_FILE):
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(Fernet.generate_key())

# Load the encryption key
with open(KEY_FILE, "rb") as key_file:
    ENCRYPTION_KEY = key_file.read()

# Initialize the Fernet encryption tool
cipher = Fernet(ENCRYPTION_KEY)

sp = None  # Spotify client

class SpotifyModel:
    def __init__(self):
        self.config_file = "config.json"
        self.key_file = "key.key"

        # Generate a key for encryption if it doesn't exist
        if not os.path.exists(self.key_file):
            with open(self.key_file, "wb") as key_file:
                key_file.write(Fernet.generate_key())

        # Load the encryption key
        with open(self.key_file, "rb") as key_file:
            self.encryption_key = key_file.read()

        # Initialize the Fernet encryption tool
        self.cipher = Fernet(self.encryption_key)

        if not os.path.exists(self.config_file):
            # Create empty config.json if it doesn't exist
            self.save_config("your_client_id", "your_client_secret")

    def save_config(self, client_id, client_secret):
        """Save Spotify Client ID and Secret to an encrypted config file."""
        data = {"client_id": client_id, "client_secret": client_secret}
        encrypted_data = self.encrypt_data(data)
        with open(self.config_file, "wb") as file:
            file.write(encrypted_data)

    def load_config(self):
        """Load Spotify Client ID and Secret from an encrypted config file."""
        if os.path.exists(self.config_file):
            with open(self.config_file, "rb") as file:
                encrypted_data = file.read()
                return self.decrypt_data(encrypted_data)
        return {"client_id": "your_client_id", "client_secret": "your_client_secret"}

    def encrypt_data(self, data):
        """Encrypt JSON data using AES encryption."""
        json_data = json.dumps(data).encode("utf-8")
        return self.cipher.encrypt(json_data)

    def decrypt_data(self, encrypted_data):
        """Decrypt AES-encrypted JSON data."""
        try:
            decrypted_data = self.cipher.decrypt(encrypted_data).decode("utf-8")
            return json.loads(decrypted_data)
        except Exception:
            return {"client_id": "your_client_id", "client_secret": "your_client_secret"}
