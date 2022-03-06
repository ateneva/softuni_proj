
'''
Create class named Music that receives title (string), artist (string) and
lyrics (string) upon initialization. The class should also have methods print_info() and play().
The print_info() method should return the following:
'This is "{title}" from "{artist}"'
The play() method should return the lyrics.
'''

class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    # method
    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    # method
    def play(self):
        return self.lyrics


song = Music("Title", "Artist", "Lyrics")
print(song.print_info())
print(song.play())
