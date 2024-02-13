from src.prompt import *
from src.chat import *

prompt = Prompt()
print(prompt.list_models())

print(prompt.ask(prompt = "Hi, how are you?"))
print(prompt.ask(prompt = "Tell me a funny joke"))
print(prompt.ask(prompt = "Which is the capital is Spain?"))
print(prompt.ask(prompt = "The population of the US is..."))

chat = Chat()
print(chat.ask(prompt = "Hi, how are you?"))
print(chat.ask(prompt = "Tell me a funny joke"))
chat.restart()
print(chat.ask(prompt = "Which is the capital is Spain?"))
print(chat.ask(prompt = "The population of the US is..."))

chat.change_template("""
    Human: The following is a friendly conversation between a human and an AI.
    The AI provides lots of specific details from its context. If the AI does not know
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
print(chat.ask(prompt = "Which is the capital is Spain?"))    

