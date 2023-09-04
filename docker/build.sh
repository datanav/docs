#!/usr/bin/env bash
set -e

# TODO switch to :rc and let promotion job promote after testing it
export TAG=${TAG-latest}
DOCKER_BUILD=${DOCKER_BUILD-1}
DOCKER_BUILD_PUSH=${DOCKER_BUILD_PUSH-0}

IMAGE_NAME=sesam/docs
export IMAGE_NAME_ACR=sesam.azurecr.io/$IMAGE_NAME

if [ $DOCKER_BUILD -eq 1 ]; then
  docker build $DOCKER_BUILD_OPTIONS -t $IMAGE_NAME:$TAG .
  docker images
fi
if [ $DOCKER_BUILD_PUSH -eq 1 ]; then
  echo "Pushing $IMAGE_NAME:$TAG"
  docker push $IMAGE_NAME:$TAG
  docker tag $IMAGE_NAME:$TAG $IMAGE_NAME_ACR:$TAG
fi
