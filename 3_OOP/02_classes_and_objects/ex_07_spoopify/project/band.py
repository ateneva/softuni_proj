'''
-	add_album(album: Album)
o	Adds an album to the collection and returns "Band {band_name} has added their newest album {album_name}."
o	If the album is already added, returns "Band {band_name} already has {album_name} in their library."

-	remove_album(album_name: str)
o	Removes the album from the collection and returns "Album {name} has been removed."
o	If the album is published, returns "Album has been published. It cannot be removed."
o	If the album is not in the collection, returns "Album {name} is not found."

-	details()
o	Returns the information of the band, with their albums, in this format:
"Band {name}
 {album details}
 ...
 {album details}"

'''


from project.song import Song
from project.album import Album

#from song import Song
#from album import Album

class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        albums_list = [a for a in self.albums if a.name == album_name]
        if albums_list:
            album = albums_list[0]
            if album.published:
                return "Album has been published. It cannot be removed."

            self.albums.remove(album)
            return f"Album {album.name} has been removed."

        return f"Album {album_name} is not found."

    def details(self):
        result = f'Band {self.name}\n'

        for a in self.albums:
            result += f'{a.details()}\n'

        return result

song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())