#!/usr/bin/env bash

if [ ! $# == 1 ]; then
  echo "Invalid parameter (must be \"deploy\", \"redeploy\" or \"uninstall\")"
  exit
fi

if [ "$1" = "deploy" ]; then
  echo deploy

elif [ "$1" = "redeploy" ]; then
  echo redeploy

elif [ "$1" = "uninstall" ]; then
  echo uninstall

else
  echo "Invalid parameter: $1 (must be \"deploy\", \"redeploy\" or \"uninstall\")"
fi
