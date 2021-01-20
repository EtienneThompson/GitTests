#!/bin/bash

GIT_COMMIT_LIST=$(git diff --name-only)
echo $GIT_COMMIT_LIST

echo "HELLO WORLD"
