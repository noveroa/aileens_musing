#!/bin/bash

VENV_NAME="test_jenkins"
PYTHON="$VENV_NAME/bin/python3"
PIP="$VENV_NAME/bin/pip"

# python3 -m venv $VENV_NAME
# $PIP install 
brew install openjdk
sudo ln -sfn /opt/homebrew/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk
export JAVA_HOME="/Library/Java/JavaVirtualMachines/openjdk.jdk/Contents/Home"
java --version

brew install jenkins-lts