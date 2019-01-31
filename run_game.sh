#!/bin/sh

./halite --replay-directory replays/ -vvv --width 32 --height 32 "python3 Mike_Bot.py" "python3 Mike_Bot.py"
echo Game Complete.  Deleting Logs.
sleep 1
rm bot*.log
