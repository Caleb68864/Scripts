#!/bin/bash
clear
COUNTER=20
until [ $COUNTER -lt 10 ]; do
du -sh *
echo Press Ctrl-C to quit
sleep 10s # Waits 10 seconds.
clear
done
