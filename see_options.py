#!/bin/python3
import os

with open("search_result.txt", "r") as infile, open("tmp_result.txt", "w") as outfile:
    for line in infile:
        index = line.find("modules")
        if index != -1:
            outfile.write(line[index + 8:])

os.replace("tmp_result.txt", "search_result.txt")
