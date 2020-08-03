#! /usr/bin/env bash

set -euo pipefail

function main() {
  startDocker
  runTests "$@"
}

function startDocker() {
  echo "Starting Docker..."
  dockerd &>/var/log/dockerd.log &

  while [ ! -S /var/run/docker.sock ]; do
    echo "Waiting for Docker to start..."
    sleep 1
  done

  echo "Docker has started."
}

function runTests() {
  echo "Running tests..."
  exec "$@"
}

main "$@"
