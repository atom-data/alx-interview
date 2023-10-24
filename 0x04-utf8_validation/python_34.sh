#!/usr/bin/env bash
 sudo apt-get install build-essential checkinstall

 sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

 cd /usr/src

 sudo wget https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tgz

sudo tar xzf Python-3.4.3.tgz

cd Python-3.4.3

sudo ./configure

sudo make altinstall

sudo python3.4 -V
