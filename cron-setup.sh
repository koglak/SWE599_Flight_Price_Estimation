#! /bin/bash

mkdir modules
pip3 install -r requirements.txt -t modules

crontab crontab.txt