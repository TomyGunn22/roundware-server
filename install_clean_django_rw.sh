#!/bin/bash
DIST_PATH="/usr/local/lib/python2.6/dist-packages"
CODE_PATH="/home/ubuntu/rwserver/trunk"
FILE_HOME=`dirname $0`
sudo rm -rf $DIST_PATH/roundwared/
sudo rm -rf $DIST_PATH/roundware/
sudo python $FILE_HOME/setup.py install
sudo cp -r $CODE_PATH/roundware/rw/templates $DIST_PATH/roundware/rw/
sudo cp -r $CODE_PATH/roundware/geoposition/templates $DIST_PATH/roundware/geoposition/