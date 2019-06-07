import json

from ibm_watson import ToneAnalyzerV3
from ibm_watson.tone_analyzer_v3 import ToneInput


class SentimentParser(object):

    def __init__(self):

        # TODO - API KEY!

        self.tone_analyzer = ToneAnalyzerV3(iam_apikey="",
                                                                url="https://gateway.watsonplatform.net/tone-analyzer/api",
                                                                version="2017-09-21")

    def parseLyrics(self, lyrics: str):
        
        result = self.tone_analyzer.tone(tone_input=lyrics, content_type="text/plain").get_result()
        
        tone_results = {}
        
        for sentence in result["sentences_tone"]: # Watson analyzes sentence by sentence
            
            if len(sentence["tones"]) == 0: # Watson did not find any tone in this sentence.
                continue

            for tone in sentence["tones"]:
                tone_results.setdefault(tone["tone_id"], [])

                tone_results[tone["tone_id"]].append(tone["score"])
                
        for tone in tone_results: # Average the results
            average = 0

            length = len(tone_results[tone])
    
            for score in tone_results[tone]:
                average += score

            average = average/length

            tone_results[tone] = average

        return tone_results
