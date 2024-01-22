#!/usr/bin/env bash

#
# You need to add your AWS credentials before executing this script
# AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ACCOUNT_ID
# AWS_DEFAULT_REGION, AWS_REGION, AWS_SESSION_TOKEN
#

set +x
export DEBIAN_FRONTEND=noninteractive

# Absolute path to this repo
SCRIPT=$(readlink -f "$0")
export REPOPATH=$(dirname "$SCRIPT" | sed 's/\/infra//')

# check if the image is already built, if not build it
if [ "$(docker images | grep base_image)" == "" ]; then
	docker build --rm=true -t base_image $REPOPATH/docker
fi

# what to do, conversation(default), test or interactive
commandline='python3 /repo/src/conversation.py'
if [ "test" == "$1" ]; then 
	commandline='python3 /repo/test/test.py'
fi
if [ "i" == "$1" ]; then 
	commandline='/bin/bash'
fi

# run the app
docker run -ti --rm -v $REPOPATH:/repo \
	-w /repo/ \
	-e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_ACCOUNT_ID \
	-e AWS_REGION -e AWS_DEFAULT_REGION -e AWS_SESSION_TOKEN \
	base_image $commandline "$@"
	#base_image /bin/bash