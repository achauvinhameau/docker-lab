#!/bin/bash

if [ -f /start.sh ]
then
   python3 /watchdog.py &
   exec bash /start.sh
else
   python3 /watchdog.py
fi
