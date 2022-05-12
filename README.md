# Finding Hidden Features Responsible for Machine Learning Failures

This repository contains the scripts used for creating subsets of the 
[CheXpert dataset](https://stanfordmlgroup.github.io/competitions/chexpert/), a large dataset of chest X-rays,
used for training and testing the model in [askovdal/top1-chexpert](https://github.com/askovdal/top1-chexpert), which is 
forked from [jfhealthcare/Chexpert](https://github.com/jfhealthcare/Chexpert), and 
refactored to train only on predicting pneumothorax cases.

The `subsets` folder contains the different CSV-files created using the scripts below.

`increment-notes.md` contains a summary of our progress throughout our process of our thesis.

## Script overview

### model.py
Contains the logic for creating subsets of the main CSV-file of the whole dataset (train.csv), both as new CSV-files and
as directories containing the actual image files.

### create-csv-from-dir.py
Creates a CSV-file from a directory of files, optionally filtering the files using a suffix, and controlling the length of the outputted CSV-file.

### concat-csvs.py
Takes 2 CSV-files as input and concatenates them into a single CSV-file. Optionally, a fraction of each CSV-file can be used instead of the whole file.

### shuffle-csv.py
Shuffles the rows of a CSV-file and overwrites the original file.

### create-train-test-split.py
Takes a CSV-file and creates two new files containing a test and train subset.
