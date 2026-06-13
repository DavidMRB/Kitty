#!/bin/bash
apt-get update
apt-get install -y ffmpeg libopus-dev libffi-dev libssl-dev python3-dev
pip install --upgrade pip
pip install -r requirements.txt
