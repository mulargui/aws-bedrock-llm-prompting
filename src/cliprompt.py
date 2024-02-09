from prompt import *

class CLIPrompt(Prompt): 
    def __init__(self, 
        model:str="amazon.titan-text-express-v1", 
        temperature:float=0.0, 
        max_tokens:int=1000,
        topP:float=1.0) :

        super().__init__(model)  
        self.temperature=temperature
        self.max_tokens=max_tokens
        self.topP=topP      
    
    def prompt(self) :
        #pormpt loop
        while True:
            #read from the command line
            question = input('Your question (or stop to end): ')

            if question == 'stop' : 
                break

            #answer from the LLM
            print('LLM: ' + self.ask(prompt = question, 
                temperature = self.temperature, 
                max_tokens = self.max_tokens, 
                topP = self.topP))        
