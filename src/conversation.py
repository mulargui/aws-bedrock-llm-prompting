from basic_ai import *
from chat import *

print(list_models())
print(answer(prompt = "Hi, how are you?"))
print(answer(prompt = "Tell me a funny joke"))
print(answer(prompt = "Which is the capital is Spain?"))
print(answer(prompt = "The population fo the US is..."))

chat = Chat()
chat.chat(text = "Hi, how are you?")
chat.chat(text = "Tell me a funny joke")
chat.chat(prompt = "Which is the capital is Spain?")
chat.chat(prompt = "The population fo the US is...")