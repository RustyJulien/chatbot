from chatterbot.logic import LogicAdapter
import random
#import re, json
#from urllib import request
# %%
class RandomSongLogicAdapter(LogicAdapter):



    def __init__(self, chatbot,**kwargs):
        super().__init__(chatbot,**kwargs)
        self.songs={
                'butterfly':17319383,
                'i can only disappoint u':17319384,
                'come as no surprise https':17319385,
                'eletric man':17319386,
                'love is':17319387,
                'soundtrack 4 2 lovers':17319388,
                'forgive me':17319389,
                'until the next life':17319390,
                'fool':17319391,
                'we are the boys':17319392,
                'goodbye':17319393,
                'the chad who loved me':4175448,
                "mansun's only love song":4175452,
                'she makes my nose bleed':4175459,
                'naked twister':4175465,
                'take it easy,chicken':4175469,
                'you, who do you hate?':4175475,
                'wide open space':4175483,
                'taxloss':4175487,
                'disgusting':4175493,
                'egg shaped fred':4175498,
                'dark mavis':4175503,
                'an open letter to the lyrical trainspotter':22243096,
                'six':22322584,
                'negative':22322585,
                'shotgun':22322586,
                'inverse midas':22322587,
                'anti everything':22322588,
                'fall out':22322589,
                'serotonin':22322590,
                'cancer':22322591,
                'witness to murder':22322592,
                'television':22322593,
                'special/blown it':22322594,
                'legacy':22322595,
                'being a girl':22322596
        }

        
    def can_process(self, statement):
       return statement.text.find("随便听点") >= 0


    def __get_song( self, song_id ):

        
        url = "https://music.163.com/#/song?id=%d" % song_id 
        
        return url

    def process(self, input_statement,additional_response_selection_parameters=None):
        rst_statement=input_statement
        song_id = self.songs[random.sample(self.songs.keys(), 1 )[0]]
        rst_statement.text = self.__get_song( song_id )
        rst_statement.confidence = 1.0

        return rst_statement

