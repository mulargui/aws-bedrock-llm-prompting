import boto3
import json

"""
    Prompt models hosted in Bedrock
"""
class Prompt :
    def __init__(self,
        model:str="amazon.titan-text-express-v1") :

        self.model=model

        session = boto3.session.Session()
        self.bedrock = boto3.client(
            service_name="bedrock-runtime",
            region_name=session.region_name
        )

    """
    Function to know the models hosted in Bedrock
    """
    @staticmethod
    def list_models() :
        #return all data of each model
        #return boto3.client(service_name="bedrock").list_foundation_models()['modelSummaries']

        #return just the name of each models
        return [model['modelId'] for model in boto3.client(service_name="bedrock").list_foundation_models()['modelSummaries']]

    """
    Function to run inference with models hosted in Bedrock
    """
    def ask(self, 
        prompt:str,  
        temperature:float=0.0, 
        max_tokens:int=1000,
        topP:float=1.0) :

        body = json.dumps({"inputText":prompt,
            "textGenerationConfig": {
                "temperature": temperature,
                "maxTokenCount": max_tokens,
                "topP": topP
            }})

        output = self.bedrock.invoke_model(body = body, 
            modelId = self.model, 
            accept = 'application/json',
            contentType = 'application/json')
    
        return json.loads(output.get("body").read()).get('results')[0].get('outputText')
