import json
import ma02spotipy.constants as const

class Song:
    def __init__(self, song_id: str, name: str, popularity: int):
        self.song_id = song_id
        self.name_of_song = name
        self.popularity = popularity

    def serialize(self, serializer):
        serializer.start_object(const.SONG, self.song_id)
        serializer.add_property(const.NAME, self.name)
        serializer.add_property(const.POPULARITY, self.popularity)

    def __str__(self):
        return "id is %s, name is %s, popularity is %s" % (self.song_id, self.name_of_song, self.popularity)


