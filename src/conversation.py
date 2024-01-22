from basic_ai import *
from chat import *

#create a LLM chat object
chat = Chat(verbose=False)

#read from the command line
while True:
    #read from the command line
    input = input('Your question: ')

    if input == 'stop' : 
        break

    #answer from the LLM
    print(chat.ask(prompt = input))

