#!/usr/bin/env bash
set -ex
docker rm -f dkos || :
docker run --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --security-opt apparmor=unconfined -d --name dkos -p 2222:22 dk/ubuntu
