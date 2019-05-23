import lyricsgenius
import json

class ArtistParser(object):

    def __init__(self, ms : int):
        # Construct a Genius object w/ the api key
        self.api_key = ""
        self.max_songs = ms
        pass

    def getArtist(self, artistName: str):
        pass
        # Get artist using genius.search_artist
        # Check artist against None, if invalid search will yield None
        # If None, return false
        # If valid, proceed to save the songs using artist.save_lyrics()
        

        
    
