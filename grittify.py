#!/usr/bin/env python
"""
File Name : grittify.py
Author: Michelle Ramsahoye
Email : m210@umbc.edu
Description:
This program will print information from the following CSV files: deadmau5_albums.csv and deadmau5_tracks.csv.
These files must be in the same directory as grittify.py and music.py (contains the classes).
deadmau5_albums.csv contains in order: album_name,album_id,release_date values, and are separated by a new line each.
deadmau5_tracks.csv contains in order: track_name,track_id,album_id values, and are separated by a new line each.

"""
import csv
from datetime import datetime, date
from sys import argv
from music import Album, Song


def get_all_albums():
    """
    Takes information from the designated csv files and initializes Album and Song class objects using that data.
    :return: a list of Album objects, each of which include a Song object
    """
    album_content = []
    song_content = []
    album_song_ids = []
    complete_albums = []
    album_filename = "deadmau5_albums.csv"
    song_filename = "deadmau5_tracks.csv"

    with open(song_filename, 'r') as t_file:
        csv_t_object = csv.reader(t_file)

        for row in csv_t_object:
            song_content.append(row)

    with open(album_filename, 'r') as a_file:
        csv_object = csv.reader(a_file)

        for row in csv_object:
            album_content.append(row)

    album_content.remove(album_content[0])
    song_content.remove(song_content[0])

    for row in album_content:
        album_song_ids.append(row[1])

    for element in album_content:

        song_list = []

        joiner = "/"
        date_list = element[2].split("-")
        new_date_list = joiner.join(date_list)

        date_object2 = datetime.strptime(new_date_list, '%Y/%m/%d')

        album_date = date.fromisoformat(element[2])
        fixed_date = album_date.strftime("%B %d,%Y")

        for i in range(0, len(song_content)):
            if element[1] == song_content[i][2]:
                a = Song(song_content[i][0], song_content[i][2], element[0], date_object2)
                song_list.append(a)
        b = Album(element[0], element[1], fixed_date, song_list)
        complete_albums.append(b)

    return complete_albums


def get_songs_by_date(after=True):
    """
    Used for determining which songs are before or after a date using Album, Song, and datetime objects.
    :param after: boolean = indicates whether the function runs to complete "after" an entered argument date or "before"
    :return: nothing; the inner functions will print the output
    """
    if len(argv) < 4:
        raise ValueError("use is python3 grittify.py album [album-name]")
    date_object = datetime.strptime(argv[3], '%m/%d/%Y')
    albums = get_all_albums()
    for album in albums:
        for song in album.songs:
            if after and song.after(date_object):
                song.print()
            if not after and song.before(date_object):
                song.print()


if __name__ == '__main__':

    if len(argv) < 2:
        raise ValueError("use is python3 grittify.py [command] [args]")
    if argv[1] == 'albums':
        albums = get_all_albums()
        for album in albums:
            album.print()
    elif argv[1] == 'album':
        if len(argv) < 3:
            raise ValueError("use is python3 grittify.py album [album-name]")
        albums = get_all_albums()
        album_name_param = argv[2]
        print("The songs on {} are:".format(album_name_param))
        for album in albums:
            if album.name == album_name_param:
                for song in album.songs:
                    song.print()
    elif argv[1] == 'songs' and len(argv) == 2:
        albums = get_all_albums()
        for album in albums:
            for song in album.songs:
                song.print()
    elif argv[1] == 'songs' and argv[2] == "after":
        get_songs_by_date(True)
    elif argv[1] == 'songs' and argv[2] == "before":
        get_songs_by_date(False)
