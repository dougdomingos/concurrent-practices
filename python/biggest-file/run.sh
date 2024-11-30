#!/bin/bash
# 
# Script for running both solutions and registering the total time.
# Author: @dougdomingos

rm runs.log
time python3 ./serial.py     | tee -a runs.log
time python3 ./concurrent.py | tee -a runs.log
