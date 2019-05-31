import os
import json
import requests

import artist
import sentiment
       
def getArtistName():
    
    name = input("Enter the Artist:\n")
    return name

def getMaxSongs():
    
    while(1):
        
        try:
            maxSongs = int(input("Enter the max number of songs(1-10)\n"))
            while maxSongs < 1 or maxSongs > 10:
                print("Invalid number!\n")
                maxSongs = int(input("Enter the max number of songs(1-10)\n"))
                
            break
        
        except ValueError:
            print("Invalid input!\n")
            continue

    return maxSongs


def main():

    artistObj = artist.ArtistParser()
    sentimentObj = sentiment.SentimentParser()
    
    artistName = getArtistName()

    maxSongs = getMaxSongs()

    result = artistObj.getArtist(artistName, maxSongs)

    while result is False:
        print("Invalid artist.\n")
        artistName = getArtistName()
        result = artistObj.getArtist(artistName, maxSongs)


    songs = [json for json in os.listdir() if json.endswith(".json")]
    for song in songs:
        # get lyrics using ["songs"][0]["lyrics"]
        
    
    
if __name__ == "__main__":
    main()
