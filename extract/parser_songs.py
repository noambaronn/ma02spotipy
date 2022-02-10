import os, json


def list_of_songs(url: str):
    list_of_songs = os.listdir(url)
    return list_of_songs


def list_of_tracks(url: str):
    songs = list_of_songs(url)
    list_of_tracks = []
    for song_file in songs:
        song = open(url + song_file)
        data = json.load(song)
        list_of_tracks.append(data)
        song.close()
    return list_of_tracks
