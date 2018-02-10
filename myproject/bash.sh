#!/bin/bash

sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt-get update
sudo apt-get install python3.6
wget https://bootstrap.pypa.io/get-pip.py
sudo python3.6 get-pip.py
pip install django
pip install mysqlclient
