# essentially we want all the albums to have the same components
# album comps = name, album id, date, songs = []
# song comps = name, album id
class Album:
    def __init__(self, name, a_id, date, songs, artist="deadmau5"):
        """
        Initializes the Album class for an object given the following attributes.
        :param name: album name
        :param a_id: album id number
        :param date: album release date
        :param songs: album Song object list
        :param artist: defaulted artist for the album
        """
        self.name = name
        self.a_id = a_id
        self.date = date
        self.songs = songs
        self.artist = artist

    def print(self):
        """
        Prints the name, artist, and date released of the Album object.
        :return: printed string with the information
        """
        return print(self.name, "by", self.artist, ", released on ", self.date)

    def songs(self):
        """
        Gives access to the songs attribute of the Album class.
        :return: a list of Song objects unique to a particular Album.
        """
        return self.songs

class Song:
    def __init__(self, name, album_id, album_name, album_date, artist="deadmau5"):
        """
        Initializes the Song class for an object given the following attributes.
        :param name: song name
        :param album_id: song id number that matches with the album it is in
        :param album_name: the name of the album that it is in
        :param album_date: the date this song was released according to the album
        :param artist: the defaulted artist for the song
        """
        self.name = name
        self.album_id = album_id
        self.album_name = album_name
        self.artist = artist
        self.album_date = album_date

    def print(self):
        """
        Prints information about the Song object and its attributes.
        :return: printed string of info
        """
        return print(self.name, " by ", self.artist, ", on ", self.album_name)

    def after(self, date):
        """
        Compares two datatime objects to determine what songs occurred after an entered date.
        :param date: datatime object from the user input
        :return: printed all of the names of the songs that fit the condition regarding release date
        """
        if self.album_date > date:
            return print(self.name, " by ", self.artist, ", on ", self.album_name)

    def before(self, date):
        """
        Compares two datetime objects to determine what songs occurred after an entered date.
        :param date: datatime object from the user input.
        :return: printed all of the names of the songs that fit in the condition regarding release date
        """
        if self.album_date < date:
            return print(self.name, " by ", self.artist, ", on ", self.album_name)
