class Playlist:
    def __init__(self, name, is_premium=None):
        self.name = name
        if is_premium is None:
            self.is_premium = False
        else:
            self.is_premium = is_premium
        self.songs_ids = []

    