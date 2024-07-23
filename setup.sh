#!/bin/bash

clear
cd /home/jack/repos/leet_code_trial || exit 1

source .venv/bin/activate
pip install -r ./requirements.txt

echo -e "====================================================\\n"
python3 src/main.py
echo -e "\\n===================================================="