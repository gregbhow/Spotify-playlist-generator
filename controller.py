class SpotifyController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Initialize the button commands
        self.view.set_generate_button_command(self.generate_and_save_playlist)
        self.view.set_settings_button_command(self.open_settings)

    def generate_and_save_playlist(self):
        """Generate and save a Spotify playlist based on user inputs."""
        try:
            # Extract track IDs from input
            urls = self.view.get_track_urls()
            if len(urls) != 10:
                raise ValueError("Please provide exactly 10 Spotify track URLs.")
            seed_tracks = self.model.extract_track_ids_from_urls(urls)

            username = self.view.get_username()
            if not username:
                raise ValueError("Please provide your Spotify username.")

            playlist_name = self.view.get_playlist_name()
            if not playlist_name:
                raise ValueError("Please provide a playlist name.")

            # Authenticate Spotify client
            self.model.authenticate_spotify()

            # Generate and save playlist
            playlist = self.model.generate_playlist(seed_tracks, target_size=500)
            self.model.save_playlist(username, playlist_name, playlist)

            self.view.show_success("Playlist created successfully!")
        except ValueError as e:
            self.view.show_error(str(e))
        except Exception as e:
            self.view.show_error(f"An error occurred: {str(e)}")

    def open_settings(self):
        """Open the settings window to update Spotify Client ID and Secret."""
        self.view.open_settings()
