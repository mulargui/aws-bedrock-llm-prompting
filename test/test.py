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
print(chat.ask(prompt = "The population fo the US is..."))