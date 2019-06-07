import os
import json

from artist import ArtistParser
from sentiment import SentimentParser

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

       
def getArtistName():
    
    name = input("Enter the Artist:\n")
    return name


def getMaxSongs():

    maxSongs = 3

    while 1:
        
        try:
            maxSongs = int(input("Enter the max number of songs(1-10)\n"))
            while maxSongs < 1 or maxSongs > 10:
                print("Invalid number!\n")
                maxSongs = int(input("\nEnter the max number of songs(1-10)\n"))
                
            break
        
        except ValueError:
            print("Invalid input!\n")
            continue

    return maxSongs


def main():

    artistObj = ArtistParser()
    sentimentObj = SentimentParser()
    
    artistName = getArtistName()

    maxSongs = getMaxSongs()

    result = artistObj.getArtist(artistName, maxSongs)

    while result is False:
        print("Invalid artist.\n")
        artistName = getArtistName()
        result = artistObj.getArtist(artistName, maxSongs)

    displayMethod = input("Display results as individual songs(Y/N)\n") # Either 1 plot per song, (Y) or 1 plot w/ averages (N)

    while displayMethod.lower() != "y" and displayMethod.lower() != "n":
        print("Invalid answer. Answer Y/N.\n")
        displayMethod = input("Display results as individual songs (Y/N)\n")
        
    songs = [json for json in os.listdir() if json.endswith(".json")]

    songResults = []
    for song in songs:

        with open(song, "r") as f:
            data = json.load(f)
            lyrics = data["songs"][0]["lyrics"]
            songName = data["songs"][0]["title"]
            name = data["artist"]
            
        output = sentimentObj.parseLyrics(lyrics) # Returns averaged values.

        songResults.append(output)

        if displayMethod.lower() == "y":

            objects = tuple(output.keys())

            y_pos = np.arange(len(objects))

            sentiment = list(output[x] for x in output)

            plt.bar(y_pos, sentiment, align='center', alpha=0.5)
            plt.xticks(y_pos, objects)
            plt.ylabel('Strength of Tone')
            plt.title('Sentiment Analysis of {0}'.format(songName))

            plt.show()
            
    averagedResults = {} # ArtistParser already returns averaged values so average everything.
    
    for song in songResults:
        for tone in song:
            averagedResults.setdefault(tone, [])

            averagedResults[tone].append(song[tone])

    for tone in averagedResults:
        average = 0

        length = len(averagedResults[tone])

        for score in averagedResults[tone]:
            average += score

        average = average / length

        averagedResults[tone] = average
        
    if displayMethod.lower() == "n":

        objects = tuple(averagedResults.keys())

        y_pos = np.arange(len(averagedResults))

        sentiment = list(averagedResults[x] for x in averagedResults)

        plt.bar(y_pos, sentiment, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Strength of Tone')
        plt.title('Averaged sentiment analysis of songs from: {0}'.format(name))

        plt.show()

    for song in songs:
        os.remove(song) # Clean up the files that were saved.
    
if __name__ == "__main__":
    main()
