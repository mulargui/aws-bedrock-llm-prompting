import boto3
import json

"""
Function to know the models hosted in Bedrock
"""
def list_models() :

    session = boto3.session.Session()

    bedrock = boto3.client(
        service_name="bedrock",
        region_name=session.region_name
    )
    return bedrock.list_foundation_models()['modelSummaries']

"""
Function to run inference with models hosted in Bedrock
"""
def answer(prompt:str, 
    model:str="amazon.titan-text-express-v1", 
    temperature:float=0.0, 
    max_tokens:int=1000,
    topP:float=1.0) :

    body = json.dumps({"inputText":prompt,
        "textGenerationConfig": {
            "temperature": temperature,
            "maxTokenCount": max_tokens,
            "topP": topP
        }})

    session = boto3.session.Session()
     
    bedrock_runtime = boto3.client(
        service_name="bedrock-runtime",
        region_name=session.region_name
    )

    output = bedrock_runtime.invoke_model(body = body, 
        modelId = model, 
        accept = 'application/json',
        contentType = 'application/json')
 
    return json.loads(output.get("body").read()).get('results')[0].get('outputText')
