from prompt import *

class CLIPrompt(Prompt): 
    def __init__(self, 
        model:str="amazon.titan-text-express-v1", 
        temperature:float=0.0, 
        max_tokens:int=1000,
        verbose:bool=True) :

        super().__init__(model, temperature, max_tokens,verbose)  
    
    def prompt(self) :
        #pormpt loop
        while True:
            #read from the command line
            question = input('Your question (or stop to end): ')

            if question == 'stop' : 
                break

            #answer from the LLM
            print('LLM: ' + self.ask(prompt = question))        
