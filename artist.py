import lyricsgenius
import json

class ArtistParser(object):

    def __init__(self):

        self.api_key = "" # IMPORTANT!!!
        self.artist = None
        
        self.genius = lyricsgenius.Genius(self.api_key)
        self.genius.verbose = False # Get rid of status messages
        self.genius.remove_section_headers = True
        self.genius.skip_non_songs = True
        self.genius.excluded_terms = ["(Remix)", "(Live)"]

    def getArtist(self, artistName: str, maxSongs: int):
        
        self.artist = self.genius.search_artist(artistName, max_songs = maxSongs, get_full_info=False)

        if self.artist is None:
            return False
        else:
            self.artist.save_lyrics()
            return True
        

        
    
