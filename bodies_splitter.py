#!/usr/local/env python
"""
Bodies splitter for Fake News Challenge
 - @alfmel

The original corpus has all bodies in one CSV file. This tool splits the train_bodies.csv files into separate files.
The files are stored in the train_bodies directory. Each article will then be written to a file called body_XXX.txt
where XXX corresponds to the unpadded Body ID. For example, the body of the article with Body ID of 4 will be in a file
called body_4.txt while the body of article with Body ID of 472 will be in body_472.txt.

The best part of all this is that the individual article files don't need to be unescaped and can be fed directly into
many tools.
"""

import csv
import os


# Define our names
bodies_file = "train_bodies.csv"
body_directory = "train_bodies"
filename_template = "body_{}.txt"

# Create directory if it doesn't already exist
if not os.path.exists(body_directory):
    os.makedirs(body_directory)

with open(bodies_file) as input_file:
    reader = csv.DictReader(input_file)
    for row in reader:
        filename = os.path.join(body_directory, filename_template.format(row["Body ID"]))
        with open(filename, "w") as output_file:
            output_file.write(row["articleBody"])
