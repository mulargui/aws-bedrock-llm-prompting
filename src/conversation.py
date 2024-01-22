from basic_ai import *
from chat import *

#create a LLM chat object
chat = Chat(verbose=False)

#read from the command line
while True:
    #read from the command line
    question = input('Your question (or stop to end): ')

    if question == 'stop' : 
        break
    if question == 'clear' : 
        chat.restart()
        continue

    #answer from the LLM
    print('LLM: ' + chat.ask(prompt = question))
