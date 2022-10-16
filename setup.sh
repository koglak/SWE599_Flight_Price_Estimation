#! /bin/bash

sudo apt-get update
sudo apt-get install -y pip
sudo apt-get install -y wget

pip3 install -r requirements.txt

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
