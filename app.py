from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot     = ChatBot('Bot')#, read_only=True)
trainer = ListTrainer(bot)

for files in os.listdir('arq'):
	data=open('arq/' + files, 'r').readlines()
	trainer.train(data)

while True:
	print('Bot :', bot.get_response( input('Você:') ) )

		
