from ma02spotipy.extract.parser_songs import *
from ma02spotipy.load.load_to_objects import *
from ma02spotipy.exceptions.exceptions import *
import ma02spotipy.constants as const


def get_albums_by_artist_id(artist_id: str):
    albums = ""
    is_exist = False
    set_of_artist, set_of_albums = load_to_objects(list_of_tracks(const.SONGS_DIRECTORY_PATH))
    for artist in set_of_artist:
        if artist.id_of_artist == artist_id:
            is_exist = True
            for album in artist.albums_of_artist:
                albums += album.name_of_album
            return albums
    if is_exist == False:
        raise ArtistNotExist


def get_songs_in_album(album_id: str):
    is_exist = False
    set_of_artists, set_of_albums = load_to_objects(list_of_tracks())
    for album in set_of_albums:
        if album.id_of_album == album_id:
            is_exist = True
            return album.songs
    if is_exist == False:
        raise AlbumNotExist


def get_all_the_artists_songs(artist_id: str):
    is_artist_exist = False
    all_the_songs_of_artist = []
    set_of_artists, set_of_albums = load_to_objects(list_of_tracks())
    for artist in set_of_artists:
        if artist.id_of_artist == artist_id:
            is_artist_exist = True
            for album in artist.albums_of_artist:
                for song in album.songs:
                    all_the_songs_of_artist.append(song)
                return all_the_songs_of_artist, is_artist_exist


def get_the_best_songs_by_popularity(artist_id: str, is_premium: bool):
    artists_songs, is_artist_exist = get_all_the_artists_songs(artist_id)
    if is_artist_exist == False:
        raise ArtistNotExist
    artists_songs = sorted(artists_songs, key=lambda song: song.popularity, reverse=True)
    if is_premium:
        return artists_songs[:10]
    else:
        return artists_songs[:5]
