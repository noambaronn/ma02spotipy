from ma02spotipy.extract.parser_songs import *
from ma02spotipy.load.load_to_objects import *
import ma02spotipy.constants as const


def get_albums_by_artist_id(artist_id: str):
    albums = ""
    set_of_artist, set_of_albums = load_to_objects(list_of_tracks(const.SONGS_DIRECTORY_PATH))
    for artist in set_of_artist:
        if artist.id_of_artist == artist_id:
            for album in artist.albums_of_artist:
                albums += album.name_of_album
            return albums
