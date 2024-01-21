from basic_ai import *
from chat import *

print(list_models())
print(run_inference(prompt = "Hi, how are you?"))
print(run_inference(prompt = "Tell me a funny joke"))
print(run_inference(prompt = "Which is the capital is Spain?"))
print(run_inference(prompt = "The population fo the US is..."))

chat = Chat()
chat.chat(prompt = "Hi, how are you?")
chat.chat(prompt = "Tell me a funny joke")
chat.chat(prompt = "Which is the capital is Spain?")
chat.chat(prompt = "The population fo the US is...")