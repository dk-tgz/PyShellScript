#!/usr/bin/env bash
set -ex
if [[ ! -f "./ssh/id_rsa" ]]; then
  ssh-keygen -f ./ssh/id_rsa
fi
docker build . -t dk/ubuntu
