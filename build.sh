#!/bin/bash
apt-get update
apt-get install -y \
  ffmpeg \
  libopus-dev \
  libopus0 \
  libffi-dev \
  libssl-dev \
  python3-dev \
  build-essential \
  git
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
