import boto3
import json

from langchain.llms.bedrock import Bedrock
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

session = boto3.session.Session()

"""
Function to know the models hosted in Bedrock
"""

bedrock = boto3.client(
    service_name="bedrock",
    region_name=session.region_name
)

def list_models() :
    return bedrock.list_foundation_models()['modelSummaries']

"""
Function to run inference with models hosted in Bedrock
"""

bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name=session.region_name
)

def run_inference(prompt:str, 
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

    output = bedrock_runtime.invoke_model(body = body, 
        modelId = model, 
        accept = 'application/json',
        contentType = 'application/json')
 
    return json.loads(output.get("body").read()).get('results')[0].get('outputText')

"""
    Function to chat with models hosted in Bedrock
"""
def chat(
    model:str="amazon.titan-text-express-v1", 
    temperature:float=0.0, 
    max_tokens:int=1000) :

    kwargs = {
        "temperature": temperature,
        "maxTokenCount": max_tokens
    }
    llm = Bedrock(
        model_id=model,
        client=bedrock_runtime,
        model_kwargs=kwargs
    )
    conversation = ConversationChain(
        llm=llm, 
        verbose=False, 
        memory=ConversationBufferMemory()
    )

    # langchain prompts do not always work with all the models.
    conversation.prompt = PromptTemplate.from_template("""
        Human: The following is a friendly conversation between a human and an AI.
        The AI is talkative and provides lots of specific details from its context. If the AI does not know
        the answer to a question, it truthfully says it does not know.

        Current conversation:
        <conversation_history>
        {history}
        </conversation_history>

        Here is the human's next reply:
        <human_reply>
        {input}
        </human_reply>

        Assistant:
    """)

    output=conversation.predict(input="Hi there!")
    print(output)
    output=conversation.predict(input="What's the weather?")
    print(output)
