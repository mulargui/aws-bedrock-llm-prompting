from basic_ai import *
from chat import *

chat = Chat(verbose=False)

#print(chat.ask(prompt = "Which is the capital is Spain?"))
chat.restart()
#print(chat.ask(prompt = "The population fo the US is..."))

#read from the command line
print('Your question:')
input = input()
print(chat.ask(prompt = input))

