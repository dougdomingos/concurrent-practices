# Biggest file by word count

## Description

We want to find out which is the **biggest file within a directory**. For that, we've implemented a
script that receives the directory path and returns the name of the file with the biggest word
count. But our script checks each file sequentially. Can you make it any faster?

Try to improve this script using multiple threads to analyze the files and, hopefully, making the
process faster.

## Instructions

1. Configure the text files by running the `setup.py` script
2. Create a new file named `concurrent.py` with your solution
3. Use the `run.sh` script to check the amount of time spent by the solutions

## Goals

- Your solution **must return the biggest file** correctly
- Your solution **should only use built-in libraries**
- You may use the provided implementation (`serial.py`) as reference to your solution
