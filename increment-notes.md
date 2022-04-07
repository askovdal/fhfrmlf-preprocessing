# Increment Notes

* [15 February](#date-15-february)
* [17 February](#date-17-february)
* [22 February](#date-22-february)
* [24 February](#date-24-february)
* [1 March](#date-1-march)
* [3 March](#date-3-march)
* [8 March](#date-8-march)
* [15 March](#date-15-march)
* [22 March](#date-22-march)
* [29 March](#date-29-march)
* [31 March](#date-31-march)
* [5 April](#date-5-April)


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
* Find out how they made the experiment for chest drain / no chest drain performance in the Hidden Strat paper ✔️
* Continue writing? 🤔


### Date: 1 March

#### What did we achieve?
* Got the classifier working and begun to move project to HPC environment.

#### What did we struggle with?
* Installing packages and getting data onto HPC

#### What would we like to work on?
* Getting the data on HPC ✔️
* Getting packages in our HPC environment (insufficient rights?) ✔️
* Trying out the classifier in the HPC environment ✔️



### Date: 3 March

#### What did we achieve?
* Got the infrastructure in HPC working with accessing data from a shared HPC folder, gotten packages installed

#### What did we struggle with?
* nothing really

#### What would we like to work on?
* Getting the data on HPC✔️
* Getting packages in our HPC environment (insufficient rights?)✔️
* Trying out the classifier in the HPC environment



### Date: 8 March

#### What did we achieve?
* Getting the data on HPC✔️
* Getting packages in our HPC environment (insufficient rights?)✔️
* Studied interpretations of chest x-rays, to get a better understanding of what we are looking at when identifying the different features of the images

#### What did we struggle with?
* It looks like the large images are too big for the classifier to train on, so we are going to look at using the small images instead

#### What would we like to work on?
* We are going to use the pretrained model to initially test a subset of pneumothorax positive cases as test set and report performance
   The model will be trained on the training data included in the code.
* Then, we are going to make two subsets, 1 with tubes and 1 without and test it to report performance, tendencies and error audit in line with Laurens paper
* Then we are going to brain storm about more intelligent test cases

### Date: 15 March

#### What did we achieve?
* Made two subsets, one with tubes and one without, and converted them into .csv-files
* Made Python scripts to create different subset CSVs from the images we examined for drainage tubes, both with and without
* Examined a lot of x-rays with pneumothorax for drainage tubes, as this is the hidden feature we have chosen to start with looking at

**TEST SPECIFICATION:**  
_The series of tests we are conduction on a small sample size is a combination of the following_  

Data generalities:  
* The split between negative and positive pneumothorax cases should be 50/50, later it can be more complex
* For cases of both tubes and no tubes, we do a (25% tube, 25% no tube | 50% negative) split

A. Training data  
* A.1 All data (Both tubes and no tubes)  
* A.2 Only with tubes  
* A.3 Only without tubes    
   
B. Test Data  
* B.1 All data (Both tubes and no tubes)  
* B.2 Only with tubes  
* B.3 Only without tubes    
      
 These 9 different experimental settings will give us an idea of model performance, the influence of the hidden features (chest tubes) and how they impact predictions.  
 
 After gaining more insight we will find out what is ideal to do going forward.

#### What did we struggle with?
* There were a lot of other people using the HPC, so we didn't have acces to the desktop that we needed to train the classifier, as it uses a lot of VRAM. We're looking into getting acces to the red queue, were there are more beefy clusters available

#### What would we like to work on?
*


### Date: 17 March

#### What did we achieve?
* Today we examined more x-ray photos, this time of patients without Pneumothorax, and identified the images that had drain tubes in them, as that are the hidden feature that we are focusing on.
* We created all the subsets detailed in the test specification, so we are ready to train and test the classifier on the different combinations and study the outcomes.

#### What did we struggle with?
* The only desktop that we can use on the HPC cluster queue that we have access to is occupied, so we sadly can't train the classifier. We've contacted ITU to see if we can get access to the red queue, where there are more computing nodes that we can use for the training.

#### What would we like to work on?
* If we can get access to the computing nodes on the HPC, we can use one of the clusters to get results from the classifier and start our research?? Pray for Lottie 🙏

#### Questions for next meeting
* Regarding our test specification - how would we go about testing with and without tubes in relation to pneumothorax negative cases? - If we only removed tubes from positive cases, then it could be creating some underlying bias in regards to tubes that are not representative of real world tendencies.

### Date: 22 March

#### What did we achieve?
* We started training and testing on the subsets mentioned last time
* We began writing on the data, specifically chexpert, defined hidden features 📝

#### What did we struggle with?
* Kasper was down bad with influenza 🫠😩
* We struggled with getting the top1-chexpert scripts to work, but we figured it out in the end

#### What would we like to work on?
* Produce some concrete results from the test specifications

### Date: 29 March

#### What did we achieve?
* We got results from the top1 classifier, training and testing on multiple different subsets of the data. We created a benchmark set with 20k random images from the dataset.

### Date: 31 March

#### What did we achieve?
* So much(!!!)
* We got performance metrics for various test specification test cases (baseline, only with tubes, only without tubes), with results that indicates that our hypothesis (taken from the hidden strat paper) were right 🎉🎉 - i.e. the performance on tubes is significantly better than without tubes. 
* We have begun writing about the theoretical architecture of our model (PCAM pooling and medical imaging applicability)
* 

#### What did we struggle with?
* A lot of people are using the HPC compute nodes, so we couldn't use as many resources as we would like, which resulted in the training and testng taking quite a bit longer than optimal. Hopefully people will stop using as many compute nodes at the same time 🙏

#### What would we like to work on?
* We can now begin to look into starting the next part of our thesis, which is looking into identifying the hidden features in the x-rays. 


### Date: 5 April

#### What did we achieve?
* We've considered the following in regards to our tests:
**Test/verify if the hidden feature performance is training induced** - It would be interesting to verify if the hightened performance is training induced, i.e. how does it perform if we remove the the tubes from the training data? Our hypothesis is, that our performance on the clinical significant cases (i.e. non-treated/no tube patients) will increase.

This however, requires more extensive image-level labelling to gain enough data to make sound training, as we have to confirm that no tubes are apparent.

* We are going to have a look (pre-meeting) at the heatmaps to see, if we can gain an insight in, where on the x-rays our model assign a high possibility of a patient being pneumothorax positive.

* Something to discuss that we can't test - how would the model perform, if a patient has had a chest drain for another reason than a pneumothorax? Do we expect it to highten the chance of a false positive classification?

* Something to talk about - we have randomized our test set to make sure the order of samples doesn't influience the classification.

* How would we go about finding tubes? What are some possible approaches?

* In doubt about how much we should write about the model as compared to the experiments itself? We have been used to writing about the models, but it seems like it is of less importance when comparing to related research.

#### What would we like to work on?
* We are going to evaluate more on our results, and write down what we have learned from our experiments.
