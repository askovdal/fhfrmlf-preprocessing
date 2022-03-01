# Increment Notes

* [15 February](#date-15-february)
* [17 February](#date-17-february)
* [22 February](#date-22-february)
* [24 February](#date-24-february)
* [1 March](#date-1-march)

### Date: 15 February

#### What did we achieve?

* We've downloaded the CheXpert data from Stanford containing 400+ gb of chest x-ray scans (~250.000 scans)
* We've set up a template for our thesis in Overleaf and gotten BibTex up and running with the papers we've touched so far
* We've gotten the GitHub infrastructure up to acceptable standards and added notes for the weekly increments

#### What did we struggle with?

* We had a hard time figuring out what data to use and how much we need
* It has been tough figuring out formal requirements? How long should the bachelor be, what style should the document be, what is required information?
* Which direction do we want to go in first and work up from?
* Which ML library should we use?

#### What would we like to work on?

* We would like to get an idea of the direction we want to go in - and start writing some code and explore the data
* We want to formalize a concrete research question to aid us in our work
* We want to make a plan for what we need to implement when
* We want to define what a hidden feature in relation to our research
* Read "Hidden Stratification Causes Clinically Meaningful
Failures in Machine Learning for Medical Imaging" and generate ideas

### Date: 17 February

#### What did we achieve?

* Found repositories containing models for classifying pathologies
* Read "Hidden Stratification Causes Clinically Meaningful Failures in Machine Learning for Medical Imaging" and generate ideas
* Set up a coding environment where we can work together in the editor 🎉

#### What did we struggle with?

* Finding the definitions for the different columns in the .csv-file for the data 🕵️‍♂️

#### What would we like to work on?

* Use the models we found, and see if we can recreate the results
* Create a subset of the data with only pneumothorax
* Make a test case for one condition (pneumothorax) and one hidden feature (tube)

### Date: 22 February

#### What did we achieve?

* Quick read paper architecture in Notion
* Check pathology matrix to see if registered support devices are correlating with tubes for a pneumothorax
* We have clarified that a drain tube does not lie under Support Devices 🥤 in the labels of the dataset, as we have found examples of the tubes appearing where the Support Devices label are categorized as both negative and positive.  
* We have thoroughly read the Hidden Stratification paper, highlighted in categories and found out, what we want to implement
* We have been trying to get a chexpert classifier work
* We have come to terms with trying to check classification behaviour on chest drain and chest drain-less pictures

#### What did we struggle with?

* Making the number 1 solution to chexpert work in our favour

#### What would we like to work?
* Things not done from todo anno 17th of february
* Get a classifier for chexpert to work (try the jupyter notebook one)
* Get a division of datasets containing chest drains and no chest drains
* Find out how they made the experiment for chest drain / no chest drain performance in the Hidden Strat paper
* Start writing? 🤔


### Date: 24 February

#### What did we achieve?

* Gotten #1 solution to run (classification model) - we just need to decompress the data
* Begun writing the related work section

#### What did we struggle with?

* Everything

#### What would we like to work?
* Things not done from todo anno 17th of february
* Get a classifier for chexpert to work (try the jupyter notebook one)
* Get a division of datasets containing chest drains and no chest drains
* Find out how they made the experiment for chest drain / no chest drain performance in the Hidden Strat paper
* Continue writing? 🤔


### Date: 1 March

#### What did we achieve?
* Got the classifier working and begun to move project to HPC environment.

#### What did we struggle with?
* Installing packages and getting data onto HPC

#### What would we like to work on?
* Getting the data on HPC
* Getting packages in our HPC environment (insufficient rights?)
* Trying out the classifier in the HPC environment
