## Author: Karthik Sunil (KCS)
## Azure function for Predicting the labels of the Softtek help tickets based on Description
## This function takes the input as trained ML model (model_stkhelp_q.bin) and text sent
## and send a JSON output with probable labels. It will also provide the probability of label prediction
## Current F1 Score is 59 with Precisiion - 89% and Recall - 42%
###########################################################################################
## Date           Author                Changes         
## 28-Jul-2020    Karthik Sunil         Initial version
## 29-Jul-2020    Karthik Sunil         Added log feature so that, debugging will be better in future
## Future Plans
## 1. Remove Stopwords from English and Spanish  NLTK - Training 
## 2. More hyperparameter adjustments while training - Training
## 3. Provide more outputs like SLA etc while predicting 
#############################################################################################
import logging
import fasttext
import azure.functions as func
import json
import re
import string

def clean_text(text):
    text = text.lower()                                                   # Make text lowercase
    text = re.sub('\[.*?\]', '', text)                                    # Remove text in square brackets    
    text = re.sub('https?://\S+|www\.\S+', ' ', text)                      # Remove hyper links
    # text = re.sub('<.*?>+', '', text)                                     # Remove texts in angular brackets <xxx>
    # text = re.sub('@.*?\s', '', text)                                     # Remove mentions in tweet
    text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)       # Remove punctuation
    text = re.sub('\n', ' ', text)                                         # Remove New line character
    # text = re.sub('\w*\d\w*', '', text)                                   # Remove words containing numbers
    return text


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    text = req.params.get('text')
    if not text:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            text = req_body.get('text')

    if text:
        logging.info(text)                                      # Log the Input Text
        model = fasttext.load_model("model_stkhelp_q.bin")      # Load the ML model 
        cleaned = clean_text(text)                              # Perform simple cleaning 
        label = model.predict(cleaned, k=3)                     # Predict the labels 
        logging.info(str(label))                                # Log the predicted labels 
        
        ## Prepare the JSON for output
        col1 = list(label[0])
        col2 = label[1].tolist()
        pairs = zip(col1, col2)
        json_values = ('"{}": {}'.format(label, value) for label, value in pairs)
        my_string = '{' + ', '.join(json_values) + '}'
        
        return func.HttpResponse(json.dumps(my_string), mimetype="application/json")
    else:
        return func.HttpResponse(
             "Please pass a value to 'text' on the query string or in the request body",
             status_code=400
        )
