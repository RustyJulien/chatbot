import chatterbot.trainers
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

from flask import Flask,render_template,request




if __name__ == "__main__":
    app=Flask(__name__)
    print("I am running")
    
    bot = chatterbot.ChatBot( "Mansun3",
                                 logic_adapters=[
                                         {'import_path': 'SongAdapter.SongLogicAdapter'},
                                         {'import_path': 'WeiboAdapter.WeiboLogicAdapter'},
                                         {'import_path': 'RandomSongAdapter.RandomSongLogicAdapter'},
                                         'chatterbot.logic.BestMatch',
                                         ],
                                 storage_adapter="chatterbot.storage.SQLStorageAdapter"
                                 )   
    app=Flask(__name__)
    
    
    ctrainer = ChatterBotCorpusTrainer(bot)

    ctrainer.train('chatterbot.corpus.chinese')
    ctrainer.train('mycorpus/')

    @app.route('/')
    def home():
        return render_template("index.html")
    @app.route("/get")
    def get_bot_response():
        userText = request.args.get('msg')
        return str(bot.get_response(userText))
    
    if __name__ == "__main__":
        app.run()
    
    print(bot.get_response('我想听wide open space'))

'''
    import itchat
    @itchat.msg_register(itchat.content.TEXT)
    def print_content(msg):
        reply=bot.get_response(str(msg['Text']))
        print(reply)
        return(reply.text)
        

    itchat.auto_login(hotReload=True)
    itchat.run()

'''
