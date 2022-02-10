import string
import secrets


def generate_secret_id():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(10))
    return password


class User():
    def __init__(self, spotify_client_key, is_premium=None, is_artist=None):
        self.user_key = spotify_client_key
        self.spotify_client_secret = generate_secret_id()
        self.playlists = []
        if is_artist is not None:
            self.is_premium = True
        else:
            self.is_artist = False
        if is_premium is None:
            self.is_premium = False
        else:
            self.is_premium = is_premium
