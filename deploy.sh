#!/usr/bin/env bash

if [ ! $# == 1 ]; then
  echo "Invalid parameter (must be \"deploy\", \"redeploy\" or \"uninstall\")"
  exit
fi

K8S_DATA_DIR=/etc/api-server-base

if [ "$1" = "deploy" ]; then
  kubectl apply -f deploy/service-account.yaml
  kubectl apply -f deploy/cluster-role-binding.yaml
  kubectl apply -f deploy/master.yaml
  kubectl apply -f deploy/worker.yaml
  kubectl apply -f deploy/master-svc.yaml
  cp -r ./src ${K8S_DATA_DIR}
  cp -r ./pkg ${K8S_DATA_DIR}

elif [ "$1" = "redeploy" ]; then
  kubectl delete -f deploy/service-account.yaml
  kubectl delete -f deploy/cluster-role-binding.yaml
  kubectl delete -f deploy/master.yaml
  kubectl delete -f deploy/worker.yaml
  kubectl delete -f deploy/master-svc.yaml

  kubectl apply -f deploy/service-account.yaml
  kubectl apply -f deploy/cluster-role-binding.yaml
  kubectl apply -f deploy/master.yaml
  kubectl apply -f deploy/worker.yaml
  kubectl apply -f deploy/master-svc.yaml
  cp -r ./src ${K8S_DATA_DIR}
  cp -r ./pkg ${K8S_DATA_DIR}

elif [ "$1" = "uninstall" ]; then
  kubectl delete -f deploy/service-account.yaml
  kubectl delete -f deploy/cluster-role-binding.yaml
  kubectl delete -f deploy/master.yaml
  kubectl delete -f deploy/worker.yaml
  kubectl delete -f deploy/master-svc.yaml

else
  echo "Invalid parameter: $1 (must be \"deploy\", \"redeploy\" or \"uninstall\")"
fi
