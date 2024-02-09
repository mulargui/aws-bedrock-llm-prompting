from chat import *

class CLIChat(Chat): 
    def __init__(self, 
        model:str="amazon.titan-text-express-v1", 
        temperature:float=0.0, 
        max_tokens:int=1000,
        verbose:bool=True) :

        super().__init__(model_id, temperature, max_tokens,verbose)  
    
    def chat() :
        #chat loop
        while True:
            #read from the command line
            question = input('Your question (or stop to end or clear to restart the conversation): ')

            if question == 'stop' : 
                break
            if question == 'clear' : 
                restart()
                continue

            #answer from the LLM
            print('LLM: ' + ask(prompt = question))        
