import os
import sys
import ma02spotipy.constants as const
from ma02spotipy.extract.parser_songs import *
from ma02spotipy.load.load_to_objects import *
from ma02spotipy.searches.searches_on_data import *
from ma02spotipy.user.user import *


def register():
    spotify_client_key = input("Put your username : ")
    is_premium = int(input("Would you like to have a premium user? "))
    if is_premium == 1:
        const.IS_PREMIUM = True
    elif is_premium == 0:
        const.IS_PREMIUM = False
    else:
        print("1 = True, 0 =False" + "\n" + "Try Again")
        menu()
    is_artist = int(input("Are you an artist? "))
    if is_artist == 1:
        const.IS_ARTIST_USER = True
    elif is_artist == 0:
        const.IS_ARTIST_USER = False
    else:
        print("1 = True, 0 =False" + "\n" + "Try Again")
        menu()
    user = User(spotify_client_key, is_premium, is_artist)
    print("Hello " + spotify_client_key)


# TODO
def login():
    pass


def menu():
    print("************Welcome to Spotipy**************")
    print()
    option = input("""
                              A: Please Register 
                              B: Login
                              C: Logout

                              Please enter your choice: """)
    if option == "A" or option == "a":
        register()
    elif option == "B" or option == "b":
        login()
    elif option == "C" or option == "c":
        sys.exit
    else:
        print("You must only select either A, B or C")
        print("Please try again")
        menu()

    choice = input("""
    
                          A: Get all artists
                          B: Get all the albums of an artist
                          C: Get the most popular songs of an artist
                          D: Get all songs in Album
                          E: Exit
    
                          Please enter your choice: """)

    if choice == "A" or choice == "a":
        set_artists, aet_albums = load_to_objects(list_of_tracks(const.SONGS_DIRECTORY_FOR_MENU))
        for artist in set_artists:
            print(artist.__str__())
            print("")
        menu()
    elif choice == "B" or choice == "b":
        artist_id = input("Put the artist id: ")
        albums = get_albums_by_artist_id(artist_id)
        for album in albums:
            print(album.__str__())
            print("")
        menu()


if __name__ == '__main__':
    menu()
