from ma02spotipy.extract.parser_songs import *
from ma02spotipy.load.load_to_objects import *
from ma02spotipy.exceptions.exceptions import *
import ma02spotipy.constants as const


def get_albums_by_artist_id(artist_id: str):
    albums = ""
    set_of_artist, set_of_albums = load_to_objects(list_of_tracks(const.SONGS_DIRECTORY_PATH))
    for artist in set_of_artist:
        if artist.id_of_artist == artist_id:
            for album in artist.albums_of_artist:
                albums += album.name_of_album
            return albums


def get_songs_in_album(album_id: str):
    is_exist = False
    set_of_artists, set_of_albums = load_to_objects(list_of_tracks())
    for album in set_of_albums:
        if album.id_of_album == album_id:
            is_exist = True
            return album.songs
    if is_exist == False:
        raise AlbumNotExist
