import lyricsgenius


class ArtistParser(object):

    def __init__(self):

        self.api_key = ""  # TODO - API KEY!!
        self.artist = None
        
        self.genius = lyricsgenius.Genius(self.api_key)
        self.genius.verbose = False  # Get rid of status messages
        self.genius.remove_section_headers = True
        self.genius.skip_non_songs = True
        self.genius.excluded_terms = ["(Remix)", "(Live)"]

    def getArtist(self, artistName: str, maxSongs: int):
        
        self.artist = self.genius.search_artist(artistName, max_songs=maxSongs, get_full_info=False)

        if self.artist is None: # Will return none if it's an invalid artist
            return False
        else:
            self.artist.save_lyrics() # Only way this lib works is to save in the same directory as the script.
            return True
