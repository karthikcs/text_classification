import nltk
from nltk.corpus import stopwords
import re


try:
    print(nltk.data.find('corpora/stopwords')) 
except LookupError:
    nltk.download('stopwords')
en_stopwords = stopwords.words('english')
es_stopwords = stopwords.words('spanish')
enes_stopwords = en_stopwords + es_stopwords

def remove_stopwords(text):
    resultwords  = [word for word in re.split("\W+",text) if word.lower() not in enes_stopwords]
    result = ' '.join(resultwords)
    return result

input_text = 'Esto es realmente asombroso. Me encanta trabajar con ese científico increíble.'

print(remove_stopwords(input_text))