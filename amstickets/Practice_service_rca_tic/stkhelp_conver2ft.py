## This program converts the file provided by Jaime Tenorio Ballesteros <jaime.tenorio@softtek.com>
## It converts to file which is needed by FastText
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
# es_stopwords = stopwords.words('spanish')
enes_stopwords = en_stopwords #+ es_stopwords
# print(enes_stopwords)    

df = pd.read_csv('ITIS_Service.csv', lineterminator='\n')
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
    return text

df['cleaned_text'] = df['Description\r'].apply(clean_text)
df['rem_stopwords_text'] = df['cleaned_text'].apply(remove_stopwords)
# df.to_csv('ups_ticket_classify_cleaned.csv')
# df1 = df.head()
print(df.head())
f = open("ITIS_Service","w+")
for index, line in df.iterrows():
    label1 = line['Label']
    # label2 = line['Label 2']
    clean_text =  line['rem_stopwords_text'].replace('\n',' ').replace('\r', ' ')
    # f.write("%s %s %s \r\n" % (label1, label2, clean_text ))
    f.write("%s %s \n" % (label1, clean_text ))
f.close()