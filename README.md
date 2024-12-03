# 🎵 Spotify Playlist Generator 🎵

Create awesome Spotify playlists effortlessly! This Python application lets you generate personalized playlists using 10 seed tracks. It features a sleek GUI, follows the MVC (Model-View-Controller) design pattern, and securely encrypts your Spotify API credentials. 🚀

---

## ✨ Features

1. 🎶 **Playlist Generation**: Build a playlist of up to 100 tracks from 10 Spotify track URLs.
2. 🔒 **Encrypted Credentials**: Secure storage for your Spotify Client ID and Secret using AES encryption.
3. ⚙️ **Customizable Settings**: Easily update your Spotify credentials from the GUI.
4. 🌟 **User-Friendly Interface**: Clean and stylish GUI to make the process smooth and fun.

---

## 🛠️ Requirements

- 🐍 **Python**: Version 3.12 or higher.
- 📱 **Spotify Developer Account**: To create a Client ID and Secret (see setup instructions below).

---

## 🚀 Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/spotify-playlist-generator.git
   cd spotify-playlist-generator
   ```

2. **Install Dependencies**:
   Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

   Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Your Spotify Developer Account**:
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
   - Create an app and retrieve your **Client ID** and **Client Secret**.
   - Add the following redirect URI in your app's settings:

     ```bash
     http://localhost:8888/callback
     ```

4. **First-Time Configuration**:
   - Run the app (see below), click the **⚙️ Settings** button, and input your **Client ID** and **Client Secret**.

---

## 🏃 How to Run

1. Run the application:

   ```bash
   python controller.py
   ```

2. Follow these steps in the GUI:
   - Paste 10 Spotify track URLs (one per line).
   - Enter your Spotify username.
   - Provide a name for the new playlist.

3. Click **Generate Playlist** 🎉 — and enjoy your personalized playlist in Spotify!

---

## 🔒 Security Notes

- Your **Client ID** and **Secret** are stored in an encrypted `config.json` file using AES encryption.
- The encryption key is stored in a separate `key.key` file.
- **Never share your `key.key` or `config.json` files publicly!**

---

## 💻 Screenshots

🎨 _Add screenshots of your application's GUI here!_

---

## 📜 License

This project is licensed under the MIT License. Feel free to use and modify it as you wish! 😄

```bash

### Updates:
- The **"How to Run"** section now references `controller.py` instead of `app.py` since your main entry point is the controller file.
- Clarified the use of the MVC structure in the **"Features"** section. 
- Updated the installation steps to include optional virtual environment setup and dependency installation.

Let me know if you need more adjustments!
