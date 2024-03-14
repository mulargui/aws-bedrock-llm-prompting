#!/usr/bin/env bash

#
# You need to add your AWS credentials before executing this script
# depending on the tool you use you will set some of the following 
# ENV variables (not all needed at the same time)
# AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ACCOUNT_ID
# AWS_DEFAULT_REGION, AWS_REGION, AWS_SESSION_TOKEN
#

set -x
export DEBIAN_FRONTEND=noninteractive

# Absolute path to this repo
SCRIPT=$(readlink -f "$0")
export REPOPATH=$(dirname "$SCRIPT" | sed 's/\/infra//')

# check if the image is already built, if not build it
if [ "$(docker images | grep llm-image)" == "" ]; then
	docker build --rm=true -t llm-image $REPOPATH/infra/docker
fi

# what to do: conversation(default), prompt, test or interactive
commandline='python3 /repo/src/main.py chat'
#in case of debugging we will expose in the container the debugging port 
debugport=''

if [ "test" == "$1" ]; then 
	commandline='python3 /repo/test/test.py'
fi
if [ "i" == "$1" ]; then 
	commandline='/bin/bash'
fi
if [ "prompt" == "$1" ]; then 
	commandline='python3 /repo/src/main.py prompt'
fi
if [ "debug" == "$1" ]; then 
	commandline='python3 /repo/src/main.py prompt debug'
	debugport='-p 5678:5678'
fi

# run the app
docker run -ti --rm -v $REPOPATH:/repo \
	-w /repo/ \
	-e PYTHONPATH='/repo' \
	-e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_ACCOUNT_ID \
	-e AWS_REGION -e AWS_DEFAULT_REGION -e AWS_SESSION_TOKEN \
	$debugport \
	llm-image $commandline
