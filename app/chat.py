from flask import Flask, render_template, request, Blueprint
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer


chat = Blueprint('chat',__name__)

conversas = [
    'oi', 
    'olá, bom dia',
    'bom dia',
    'bom dia, como vai?',
    'Como vai você ?'
    'Estou bem',
    'Qual o seu nome?',
    'Meu nome é Marcos.' 
    ]

filmes = [
    'Qual o tipo de filme que você gosta?','Eu gosto de ação'
]

bot = ChatBot('teste')
bot.set_trainer(ListTrainer)

bot.train(conversas)
bot.train(filmes)

@chat.route('/')
def home():
    return render_template('home.html')

@chat.route('/get')
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))

