#!/usr/bin/env bash
set -e

TAG=${TAG-rc}
DOCKER_BUILD=${DOCKER_BUILD-1}
DOCKER_BUILD_PUSH=${DOCKER_BUILD_PUSH-0}

IMAGE_NAME=sesam/docs

if [ $DOCKER_BUILD -eq 1 ]; then
  docker build $DOCKER_BUILD_OPTIONS -t $IMAGE_NAME:$TAG .
  docker images
fi
if [ $DOCKER_BUILD_PUSH -eq 1 ]; then

  docker push $IMAGE_NAME:$TAG
fi
