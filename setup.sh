#! /bin/bash

sudo apt-get update
sudo apt-get install -y pip3 

pip3 install -r requirements.txt -t modules
