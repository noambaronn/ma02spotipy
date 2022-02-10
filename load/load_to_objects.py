from typing import List, Dict

from ma02spotipy.objects.song import Song
import ma02spotipy.constants as const


def load_to_objects(list_of_tracks: List[Dict[str, str]]):
    list_of_artists = []
    list_of_albums = []
    for track in list_of_tracks:
        track_dict = track[const.TRACK]
        artist = put_vars_to_artist(track_dict[const.ARTISTS])
        album = put_vars_to_album(track_dict[const.ALBUM])
        song_obj = Song(track_dict[const.ID], track_dict[const.NAME], track_dict[const.POPULARITY])
        album_exist(list_of_albums, album, song_obj)
        artist_exist(list_of_artists, artist, album)
    return list_of_artists, list_of_albums


def artist_exist(list_of_artist: List[Artist], a: Artist, album: Album):
    if len(list_of_artist) == 0:
        a.albums_of_artist.append(album)
        list_of_artist.append(a)
    else:
        is_exist = False
        for artist in list_of_artist:
            if artist.name_of_artist == a.name_of_artist:
                is_exist = True
        if not is_exist:
            a.albums_of_artist.append(album)
            list_of_artist.append(a)
        else:
            a.albums_of_artist.append(album)


def album_exist(list_of_albums, a: Album, song: Song):
    if len(list_of_albums) == 0:
        a.songs.append(song)
        list_of_albums.append(a)
    else:
        is_exist = False
        for album in list_of_albums:
            if album.name_of_album == a.name_of_album:
                is_exist = True
                album.songs.append(song)
        if not is_exist:
            a.songs.append(song)
            list_of_albums.append(a)
        else:
            a.songs.append(song)


def put_vars_to_artist(artist: List[Dict[str, str]]):
    artist_dict = artist[0]
    artist_obj = Artist(artist_dict[const.ID], artist_dict[const.NAME])
    return artist_obj


def put_vars_to_album(album_dict: Dict[str, str]):
    album_obj = Album(album_dict[const.ID], album_dict[const.NAME])
    return album_obj
