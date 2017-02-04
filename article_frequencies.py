#!/usr/local/env python
"""
Tool for calculating article Body ID frequency use
 - @alfmel

The body_splitter.py script showed there were only 1,683 article bodies. That implies a many-to-many relationship
between article headlines and the article bodies.

This tool analyzes the train_stances.csv file and extracts the unique Body IDs, displaying them and the number of times
they are used. I used this tool to ensure the body_splitter.py script got all bodies and to confirm the above hypothesis
about the relationship of article headlines and bodies.
"""

import csv


filename = "train_stances.csv"
freq_map = {}

# Get the Body IDs and their frequencies
with open(filename) as file:
    reader = csv.DictReader(file)
    for row in reader:
        body_id = row["Body ID"]
        if body_id in freq_map:
            freq_map[body_id] += 1
        else:
            freq_map[body_id] = 1

# Print the results
total = 0
for key in sorted(freq_map.keys()):
    print("{} => {}".format(key, freq_map[key]))
    total += freq_map[key]

print("Total articles: {}".format(total))
print("Total article bodies: {}".format(len(freq_map.keys())))
