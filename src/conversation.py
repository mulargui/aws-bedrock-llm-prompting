from basic_ai import *
from chat import *

print(list_models())
print(ask(prompt = "Hi, how are you?"))
print(ask(prompt = "Tell me a funny joke"))
print(ask(prompt = "Which is the capital is Spain?"))
print(ask(prompt = "The population fo the US is..."))

chat = Chat()
chat.ask(prompt = "Hi, how are you?")
chat.ask(prompt = "Tell me a funny joke")
chat.ask(prompt = "Which is the capital is Spain?")
chat.ask(prompt = "The population fo the US is...")