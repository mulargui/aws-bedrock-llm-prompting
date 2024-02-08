from prompt import *

#create a LLM prompt object
tmp = Prompt()

#read from the command line
while True:
    #read from the command line
    question = input('Your question (or stop to end): ')

    if question == 'stop' : 
        break

    #answer from the LLM
    print('LLM: ' + tmp.ask(prompt = question))
