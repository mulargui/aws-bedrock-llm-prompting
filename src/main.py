from cliprompt import *
from clichat import *    
import debugpy
import sys

if (len(sys.argv) == 1 or
    len(sys.argv) > 3) :
    print(f"Usage: {sys.argv[0]} chat|prompt [debug]")
    exit()

if (sys.argv[1] != 'chat' and 
    sys.argv[1] != 'prompt') :
    print(f"Usage: {sys.argv[0]} chat|prompt [debug]")
    exit()

if (len(sys.argv) == 3 and
    sys.argv[2] != 'debug') :
    print(f"Usage: {sys.argv[0]} chat|prompt [debug]")
    exit()

#debugging mode
if len(sys.argv) == 3 :
    debugpy.listen(("0.0.0.0", 5678))
    print("Waiting for client to attach...")
    debugpy.wait_for_client()

if sys.argv[1] == 'chat' :
    #create a LLM chat object
    chat = CLIChat()

    #chat using the command line
    chat.chat()
else :
    #create a LLM prompt object
    prompt = CLIPrompt()

    #prompt using the command line
    prompt.prompt()