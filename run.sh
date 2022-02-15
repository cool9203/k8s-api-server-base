#!/usr/bin/env bash

DOCKERHUB_USER=yogawulala
IMAGE_NAME=k8s-api-server-base
DOCKERFILE_PATH=./docker/Dockerfile

if [ ! $# == 1 ]; then
  echo "Invalid parameter (must be \"build\", \"run\" or \"clear\")"
  exit
fi

if [ "$1" = "build" ]; then
  docker build . -f ${DOCKERFILE_PATH} -t ${DOCKERHUB_USER}/${IMAGE_NAME}

elif [ "$1" = "run" ]; then
  docker build . -f ${DOCKERFILE_PATH} -t ${DOCKERHUB_USER}/${IMAGE_NAME}
  ./deploy.sh redeploy

elif [ "$1" = "clear" ]; then
  docker image prune

else
  echo "Invalid parameter (must be \"build\", \"run\" or \"clear\")"
fi
