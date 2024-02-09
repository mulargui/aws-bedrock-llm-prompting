import boto3
import json

from langchain.llms.bedrock import Bedrock
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

"""
    Chat with models hosted in Bedrock
"""
class Chat :
    def __init__(self, 
        model:str="amazon.titan-text-express-v1", 
        temperature:float=0.0, 
        max_tokens:int=1000,
        verbose:bool=True) :

        kwargs = {
            "temperature": temperature,
            "maxTokenCount": max_tokens
        }

        session = boto3.session.Session()

        bedrock_runtime = boto3.client(
            service_name="bedrock-runtime",
            region_name=session.region_name
        )

        llm = Bedrock(
            model_id=model,
            client=bedrock_runtime,
            model_kwargs=kwargs
        )

        self.memory = ConversationBufferMemory()
        self.conversation = ConversationChain(
            llm=llm, 
            verbose=verbose, 
            memory= self.memory
        )

        # default langchain prompts do not always work with all the models.
        self.conversation.prompt = PromptTemplate.from_template("""
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
    """
    Function to run inference with models hosted in Bedrock
    """
    def ask(self, prompt:str) : 
        return self.conversation.predict(input = prompt)

    """
    Function to clear previous conversations
    """
    def restart(self) :
        self.memory.clear()
