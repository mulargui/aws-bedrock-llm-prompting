# aws-bedrock-llm-prompting
This repo contains a basic infrastructure to interact with AWS Bedrock LLM models. With this repo you can prompt or chat with an AWS LLM model from the command line. Prompting has no memory of past questions whereas chatting includes previous conversations and should provide richer results. This is fundational work that I will extend in the future.

To use this repo you just need git (to clone this repo) and docker. In order to access AWS you need to have environment variables with your credentials. Look at AWS documentation for the different ways to share credentials. Use something like \
export AWS_ACCESS_KEY_ID=1234567890\
export AWS_SECRET_ACCESS_KEY=ABCDEFGHIJKLMN\
export AWS_ACCOUNT_ID=1234567890\
export AWS_DEFAULT_REGION=us-east-1\
export AWS_REGION=$AWS_DEFAULT_REGION

At this time you need to activate access to Bedrock for your AWS account, I did it using the AWS console. You also need to request access to each model you want to use. I also did it using the AWS console. Keep in mind that the model access request is per region, so the AWS_REGION env var needs to match the region you requested access to the model. There is a list_models() method that return the list of models you have access in a region. You can see an example of use in test/test.py

Directories and files\
test.sh - you probably want to start here. If you can run this shellscript it means that you have everything in place and can start using this repo\
chat.sh and prompt.sh - allows you to interact with an AWS LLM from the command line.\
debug.sh - a shellscript to start the app in debug mode.\
/infra/docker/dockerfile - how to build the docker image.\
/infra/run.sh - creates the docker image on the fly and supports five modes: chat, prompt, test, debug and interactive (for inspection inside the docker container).\
/src/chat.py and prompt.py - These are base classes (in python) to prompt or chat with an LLM.  These classes encapsulate all the logic to use AWS Bedrock APIs.\
/src/clichat.py and cliprompt.py - Extends the base classes adding command line support.\
/src/main.py - entry point to the app, it just creates the objects to start with.\
/test/test.py - some basic tests to validate that all works!\
.vscode/launch.json - configuration to attach vs code debugger to the container. Look at vs code documentation on how to install and attach the python debugger to an app. https://code.visualstudio.com/docs/editor/debugging

Have fun using this repo!
