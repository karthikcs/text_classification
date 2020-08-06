# Sentiment Analyser Tool
## A webapp for analysing sentiments and getting user feedback on predeicted sentiment
---

## Functionality 

- This tool is gets a user text and predicts the sentiment using a pre-trained ML model. 
- After predicting tool provides an opportunity to user to correct the predicted sentiment
- Any user can provide the sentence and also correct the predicted sentiment. Login is not required for this feature
- All the user inputs and feedback on prediction is saved in a database and later a verified user can login and re-train the model. Re-training creates a new version of the ML model
- The latest model is based on ```amazonreviews ``` dataset which has millions of records for training. 


## Technology 
The webapp is developed using Python Django framework. Following are the technical details 

- Name of the webapp : getsentiment
- Application name: sentiapp
- Nomenclature of model: ```model_senti.bin```
- Versions of the model: ```model_senti_vXX.bin``` where XX - represents the version number
- Program to retrain the model - ```senti_retrain.py```. This module is triggered using CLI from within the webapp, when retraining is requested by authorised user. It automatically creates ```senti.train``` ```senti.test``` and ```senti.all``` files for retraining. 
- The model used is from huge dataset and size of model was more than 2.5 GB so it has been quantized using FastText ```quantize ``` option. Please refer to ```quantize_model.py```
- Database: As part of default Django framework, ```db.sqlite3``` is used as database which contains all the sentences entered by the user from webapp interface. It also contains predicted and corrected sentiment. It also tracks the sentences which were used for retraining.
- Table strcuture 
```
sqlite> pragma table_info('sentiapp_sentimenttexts');
cid         name        type        notnull     dflt_value  pk        
----------  ----------  ----------  ----------  ----------  ----------
0           id          integer     1                       1         
1           sentence    text        1                       0         
2           detected_s  varchar(1)  1                       0         
3           manual_sen  varchar(1)  1                       0         
4           confidence  real        1                       0         
5           retrain     bool        1                       0         
```
- Following command is used to start the server 
``` gunicorn --bind 0.0.0.0:8001 getsentiment.wsgi ```
- If you want to disconnect from SSH but still keep running the server, following commands will be run  
``` 
screen 
gunicorn --bind 0.0.0.0:8001 getsentiment.wsgi 
ctrl a, d (This will disconnect the server from SSH session)
```
You will be a message like ```[detached from 1704.pts-0.machine-learning2-n1-2vcpu-75]```

Now you can disconnect from SSH but still server runs without any issues. 

- To connect back to running server, run ```screen -r```
- The training dataset should have labels ```__label__1``` for negative sentiment, ```__label__2``` for postive sentiment and ```__label__0``` for neutral ones.





