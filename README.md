
# Using FastText for text classification

**Reference** : [Followed this article to start with cooking relates text classification](https://fasttext.cc/docs/en/supervised-tutorial.html)

---

Following are the few initiatives which are there in this repo
 - Cooking from Stack Exchange - As part of FastText Tutorial
	 - Python Program: ```cooking_text_classifier.py```
	 - Original Data: ```cooking.stackexchange.txt```
	 - Training Data: ```cooking.train```
	 - Testing Data :  ```cooking.test```
	 - Model File: ```model_cooking.bin```

- Sentiment Analysis using Amazon reviews
	- Python Program: ```amazon_review.py```
	- Original Data: ```amazon_reviews.txt```
	- Training Data: ```amazon.train```
	- Testing Data :  ```amazon.test```
	- Model File: ```model_amazon.bin```

- SAP Ticket Classification 
	- Python Program: ```sap_ticket_cat.py```
	- Original Data: ```sap_ticket_cat.txt```
	- Training Data: ```sap_ticket_cat.txt``` 
	- Testing Data :  Did not use validation process as sample size is very small
	- Model File: ```model_sap_ticket.bin```
## Creation of train and test data
We use following command to create train and test data 
```
head -950 amazon_reviews.txt > amazon.train
tail -50 amazon_reviews.txt > amazon.test
```
which creates a training set of 950 records from beginning and last 50 records was considered as testing records (Validation records) 

## Execution 
Following are the arguments that can be passed to our python programs

```
usage: sap_ticket_cat.py [-h] [-t] [-p SENTENCE] [-v VALIDATION] [-k K VALUE]

optional arguments:
  -h, --help     show this help message and exit
  -t             Train mode
  -p SENTENCE    Predict the class of a sentence
  -v VALIDATION  Validate the model
  -k K VALUE     Validate the model
```
Example
*Training* 
```
python3 sap_ticket_cat.py -t
```
*Evaluation*
```
python3 amazon_review.py -v amazon.test
```
Output will be something like this 
```
(50, 0.84, 0.84)
```
Which means it has 50 records to validate, 84% was Precision and 84% was Recall

*Testing*
```
python3 sap_ticket_cat.py -p "unwanted print files"
```

---

## Using FastText as Smart Categorization
**SmartCat** is one of the important goals of our Automation team. FastText's ability to categorize texts based on Supervised learning is very helpful for **SmartCat** solution. Goal of of this is to produce pre-trained models which learns from  the historical ticket data and categorizes the tickets based on the descriptions. 

Following are the sample outputs of the predictions 
```
python3 sap_ticket_cat.py -p "Please provide access to Clarence for transaction code VKB1"
Warning : `load_model` does not return WordVectorModel or SupervisedModel any more, but a `FastText` object which is very similar.
(('__label__role_admin', '__label__security', '__label__report', '__label__user_admin', '__label__maintenance'), array([0.40538526, 0.21373558, 0.04747315, 0.04416246, 0.03287791]))
```
We can see it has properly categorized as **Role Administration**  under **Security Module**

Another one 
```
python3 sap_ticket_cat.py -p "Job KA1K failed, please re-process"
Warning : `load_model` does not return WordVectorModel or SupervisedModel any more, but a `FastText` object which is very similar.
(('__label__job_mgmt', '__label__basis', '__label__maintenance', '__label__db_admin', '__label__performance'), array([8.63456488e-01, 1.34632096e-01, 4.76637826e-04, 3.39805934e-04,
       1.57182891e-04]))
```
Perfectly determined as **Job Management** under **Basis**

## Saved Models
To make sure we don't lose the good models, as a practice, good saved models are manually moved to directory ```./saved_model```

## Future plans
Following are in plan as of 14-May-2020

- Understand Word Embeddings in FastText and see how we can use them
- Work on unsupervised model of FastText
- Work on Pre-Trained Models of FastText from [here](https://fasttext.cc/docs/en/english-vectors.html)
