## This program converts the file provided by Jaime Tenorio Ballesteros <jaime.tenorio@softtek.com>
## It converts to file which is needed by FastText
## Features
## 1. Remove Stop words from English and Spanish

## Ideas to be implemented
## 1. Remove numbers from corpus: model_stkhelp_q2 : It is observed that there are a lot of numbers in the word list of the dictionary
##    Total words in the model - 55317
##    Total words with number  - 17395
##    Total words with only number - 10075
##  I am sure these words with number like sd241310, lstkeg241087 don't add value. Instead I will be removing numbers
##  to make sd, lstkeg etc. Also only numbers will be removed.
## 

import pandas as pd
import re
import string
import nltk
from nltk.corpus import stopwords

try:
    print(nltk.data.find('corpora/stopwords')) 
except LookupError:
    nltk.download('stopwords')
en_stopwords = stopwords.words('english')
es_stopwords = stopwords.words('spanish')
enes_stopwords = en_stopwords + es_stopwords
# print(enes_stopwords)    

df = pd.read_csv('stkhelp.csv', lineterminator='\n')
# print(df[0:5])

def remove_stopwords(text):
    resultwords  = [word for word in re.split("\W+",text) if word not in enes_stopwords]
    result = ' '.join(resultwords)
    return result

def clean_text(text):
    text = text.lower()                                                   # Make text lowercase
    text = re.sub('\[.*?\]', '', text)                                    # Remove text in square brackets    
    text = re.sub('https?://\S+|www\.\S+', ' ', text)                      # Remove hyper links
    # text = re.sub('<.*?>+', '', text)                                     # Remove texts in angular brackets <xxx>
    # text = re.sub('@.*?\s', '', text)                                     # Remove mentions in tweet
    text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)       # Remove punctuation
    # text = re.sub('\n', '', text)                                         # Remove New line character
    # text = re.sub('\w*\d\w*', '', text)                                   # Remove words containing numbers
    # text = re.sub('\s\d+', '', text)                                   # Remove words with only numbers 
    text = re.sub('\d+', ' ', text)                                   # Remove only numbers and numbers in words
    return text

df['cleaned_text'] = df['Description\r'].apply(clean_text)
df['rem_stopwords_text'] = df['cleaned_text'].apply(remove_stopwords)

# df1 = df.head()
f = open("stkhelp_ft","w+")
for index, line in df.iterrows():
    label1 = line['Label 1']
    label2 = line['Label 2']
    clean_text =  line['rem_stopwords_text'].replace('\n',' ').replace('\r', ' ')
    f.write("%s %s %s \r\n" % (label1, label2, clean_text ))
f.close()