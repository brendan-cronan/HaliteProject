#!/bin/sh

./halite --replay-directory replays/ -vvv  --no-replay --no-logs --width 32 --height 32 "python3 First_Bot.py" "python3 Base_Bot.py"
echo Game Complete.  Deleting Logs.
sleep 1
rm bot*.log
