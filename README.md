# aws-bedrock-llm-prompting
This repo contains a basic infrastructure to interact with AWS Bedrock LLM models. With this repo you can prompt or chat with an AWS LLM model from the command line. Prompting has no memory of past questions whereas chatting includes previous conversations and should provide richer results. This is fundational work that I will extend in the future.

To use this repo you just need git (to clone this repo) and docker. In order to access AWS you need to have environment variables with your credentials. Look at AWS documentation for the different ways to share credentials. Use something like \
export AWS_ACCESS_KEY_ID=1234567890\
export AWS_SECRET_ACCESS_KEY=ABCDEFGHIJKLMN\
export AWS_ACCOUNT_ID=1234567890\
export AWS_DEFAULT_REGION=us-east-1\
export AWS_REGION=$AWS_DEFAULT_REGION

Directories and files\
test.sh - you probably want to start here. If you can run these test it means that you have everything in place and can start using this repo\
chat.sh and prompt.sh - allows you to interact with an AWS LLM from the command line.\
/infra/docker/dockerfile - how to build the docker image.\
/infra/run.sh - creates the docker image on the fly and supports five modes: chat, prompt, test, debug and interactive (for inspection inside the docker container).\
/src/chat.py and prompt.py - These are base classes (in python) to prompt or chat with an LLM.  These classes encapsulate all the logic to use AWS Bedrock APIs.\
/src/clichat.py and cliprompt.py - Extends the base classes adding command line support.\
/src/conversation.py and questions.py - Just creates the objects to start with.\
/test/test.py - some basic tests to validate that all works!\
.vscode/launch.json configuration to attach vs code debugger to the container. Look at vs code documentation on how to install and attach the python debugger to an app

Have fun using this repo!