## Ideas to be implemented
## 
import argparse
import fasttext
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
    # text = re.sub('\s\d+', '', text)                                   # Remove numbers
    text = re.sub('\d+', ' ', text)                                   # Remove only numbers and numbers in words    
    return text


parser = argparse.ArgumentParser()
parser.add_argument('-t', action='store_true', default=False,
                    dest='do_training',
                    help='Train mode')
parser.add_argument('-p', action='store', dest='sentence',
                    help='Predict the class of a sentence') 
parser.add_argument('-v', action='store', dest='validation',
                    help='Validate the model') 
parser.add_argument('-k', action='store', dest='K Value',
                    help='Validate the model')                     

results = parser.parse_args()

if results.do_training :
    # model = fasttext.train_supervised(input="stkhelp.train", autotuneValidationFile='stkhelp.test', autotuneDuration=3600)
    model = fasttext.train_supervised(input="stkhelp.train", 
                                    wordNgrams=3,
                                    autotuneValidationFile='stkhelp.test', 
                                    autotuneDuration=3600)
    model.save_model("model_stkhelp.bin")
elif results.sentence != None :
    # model = fasttext.load_model("model_amazon_q.bin")
    model = fasttext.load_model("model_stkhelp_q.bin")
    text = clean_text(results.sentence)
    label = model.predict(text, k=3)
    str_label = str(label)
    # print(str_label)
    # jsonstr = json.dumps(label)
    col1 = list(label[0])
    col2 = label[1].tolist()
    print(col1)
    print(col2)
    pairs = zip(col1, col2)
    json_values = ('"{}": {}'.format(label, value) for label, value in pairs)
    my_string = '{' + ', '.join(json_values) + '}'
    print(json.dumps(my_string))
    
elif results.validation != None:
    # model = fasttext.load_model("model_amazon_q.bin")
    model = fasttext.load_model("model_stkhelp.bin")
    print(model.test(results.validation))