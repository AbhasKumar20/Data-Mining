#!/bin/sh

echo "Wprking on Question 1"
echo "neighbor-districts-modified.json. is in Folder Question1"

bash ./Question2/case-generator.sh
bash ./Question3/edge-generator.sh
bash ./Question4/neighbor-generator.sh
bash ./Question5/state-generator.sh
bash ./Question6/zscore-generator.sh
bash ./Question7/method-spot-generator.sh
bash ./Question8/top-generator.sh

