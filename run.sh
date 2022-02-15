#!/usr/bin/env bash

DOCKERHUB_USER=yogawulala
TEST_IMAGE_NAME=k8s-api-server-base
MASTER_IMAGE_NAME=k8s-api-server-base-master
WORKER_IMAGE_NAME=k8s-api-server-base-worker

TEST_DOCKERFILE_PATH=./docker/test/Dockerfile
MASTER_DOCKERFILE_PATH=./docker/master/Dockerfile
WORKER_DOCKERFILE_PATH=./docker/worker/Dockerfile

if [ ! $# == 1 ]; then
  echo "Invalid parameter (must be \"build\", \"run\" or \"clear\")"
  exit
fi

if [ "$1" = "build" ]; then
  docker build . -f ${MASTER_DOCKERFILE_PATH} -t ${DOCKERHUB_USER}/${MASTER_IMAGE_NAME}
  docker build . -f ${WORKER_DOCKERFILE_PATH} -t ${DOCKERHUB_USER}/${WORKER_IMAGE_NAME}

elif [ "$1" = "run" ]; then
  docker build . -f ${MASTER_DOCKERFILE_PATH} -t ${DOCKERHUB_USER}/${MASTER_IMAGE_NAME}
  docker build . -f ${WORKER_DOCKERFILE_PATH} -t ${DOCKERHUB_USER}/${WORKER_IMAGE_NAME}
  ./deploy.sh

elif [ "$1" = "master" ]; then
  docker build . -f ${TEST_DOCKERFILE_PATH} -t ${DOCKERHUB_USER}/${TEST_IMAGE_NAME}
  docker run -it --rm -v $(pwd)/setting:/setting -v $(pwd)/src/master/main.py:/main.py -v $(pwd)/pkg:/pkg -v $(pwd)/log:/log ${DOCKERHUB_USER}/${TEST_IMAGE_NAME}

elif [ "$1" = "worker" ]; then
  docker build . -f ${TEST_DOCKERFILE_PATH} -t ${DOCKERHUB_USER}/${TEST_IMAGE_NAME}
  docker run -it --rm -v $(pwd)/setting:/setting -v $(pwd)/src/worker/main.py:/main.py -v $(pwd)/pkg:/pkg -v $(pwd)/log:/log ${DOCKERHUB_USER}/${TEST_IMAGE_NAME}

elif [ "$1" = "clear" ]; then
  docker image prune

else
  echo "Invalid parameter (must be \"build\", \"run\" or \"clear\")"
fi
