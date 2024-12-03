import tkinter as tk
from tkinter import scrolledtext, messagebox
from tkinter.font import Font

class SpotifyView:
    def __init__(self, root):
        self.root = root
        self.root.title("Spotify Playlist Generator")
        self.root.geometry("500x600")
        self.root.config(bg="#2C2F33")  # Dark background

        # Custom Fonts
        self.header_font = Font(family="Helvetica", size=16, weight="bold")
        self.label_font = Font(family="Helvetica", size=12)
        self.button_font = Font(family="Helvetica", size=12, weight="bold")

        # Header
        self.header = tk.Label(root, text="🎵 Spotify Playlist Generator 🎵", font=self.header_font, bg="#2C2F33", fg="#FFFFFF")
        self.header.pack(pady=20)

        # Instructions
        self.instructions = tk.Label(root, text="Enter 10 Spotify Track URLs (one per line):", font=self.label_font, bg="#2C2F33", fg="#FFFFFF")
        self.instructions.pack(pady=5)

        # Input field for track URLs
        self.text_input = scrolledtext.ScrolledText(root, width=40, height=10, bg="#23272A", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.text_input.pack(pady=10)

        # Username entry
        self.username_label = tk.Label(root, text="Spotify Username:", font=self.label_font, bg="#2C2F33", fg="#FFFFFF")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(root, width=30, bg="#23272A", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.username_entry.insert(0, "") 
        self.username_entry.pack(pady=5)

        # Playlist name entry
        self.playlist_name_label = tk.Label(root, text="Playlist Name:", font=self.label_font, bg="#2C2F33", fg="#FFFFFF")
        self.playlist_name_label.pack(pady=5)
        self.playlist_name_entry = tk.Entry(root, width=30, bg="#23272A", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.playlist_name_entry.insert(0, "") 
        self.playlist_name_entry.pack(pady=5)

        # Generate button with hover effect
        self.generate_button = tk.Button(root, text="Generate Playlist", command=None, bg="#99AAB5", fg="#2C2F33", font=self.button_font, relief="flat")
        self.generate_button.pack(pady=20)

        # Apply hover effect for buttons
        self.apply_button_hover_effect(self.generate_button)

        # Settings button with hover effect
        self.settings_button = tk.Button(root, text="⚙️ Settings", command=None, bg="#99AAB5", fg="#2C2F33", font=self.button_font, relief="flat")
        self.settings_button.pack(pady=10)

        # Apply hover effect for settings button
        self.apply_button_hover_effect(self.settings_button)

    def apply_button_hover_effect(self, button):
        """Apply hover effect to buttons, ensuring text stays visible."""
        original_bg = button.cget("bg")
        original_fg = button.cget("fg")

        button.bind("<Enter>", lambda e: button.config(bg="#5E6B8E", fg="#FFFFFF"))  # Darker shade on hover, text stays white
        button.bind("<Leave>", lambda e: button.config(bg=original_bg, fg=original_fg))  # Revert to original button colors on leave

    def get_track_urls(self):
        """Return the track URLs entered by the user."""
        return self.text_input.get("1.0", tk.END).strip().splitlines()

    def get_username(self):
        """Return the Spotify username entered by the user."""
        return self.username_entry.get().strip()

    def get_playlist_name(self):
        """Return the playlist name entered by the user."""
        return self.playlist_name_entry.get().strip()

    def show_error(self, message):
        """Display an error message."""
        messagebox.showerror("Error", message)

    def show_success(self, message):
        """Display a success message."""
        messagebox.showinfo("Success", message)

    def set_generate_button_command(self, command):
        """Set the command to be executed when the 'Generate Playlist' button is clicked."""
        self.generate_button.config(command=command)

    def set_settings_button_command(self, command):
        """Set the command to be executed when the 'Settings' button is clicked."""
        self.settings_button.config(command=command)

    def open_settings(self):
        """Open the settings window to update Spotify Client ID and Secret."""
        def save_credentials():
            client_id = self.client_id_entry.get().strip()
            client_secret = self.client_secret_entry.get().strip()
            self.model.save_config(client_id, client_secret)
            self.show_success("Client ID and Secret updated successfully!")
            settings_window.destroy()

        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")
        settings_window.geometry("300x200")

        # Client ID
        client_id_label = tk.Label(settings_window, text="Client ID:")
        client_id_label.pack(pady=5)
        self.client_id_entry = tk.Entry(settings_window)
        self.client_id_entry.pack(pady=5)
        self.client_id_entry.insert(0, "") 

        # Client Secret
        client_secret_label = tk.Label(settings_window, text="Client Secret:")
        client_secret_label.pack(pady=5)
        self.client_secret_entry = tk.Entry(settings_window)
        self.client_secret_entry.pack(pady=5)
        self.client_secret_entry.insert(0, "") 

        # Save button
        save_button = tk.Button(settings_window, text="Save", command=save_credentials)
        save_button.pack(pady=10)
