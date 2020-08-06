from django.shortcuts import render
from .models import SentimentTexts
from django.http import HttpResponseRedirect 
import fasttext
from django.views.generic import TemplateView
# from getsentiment.urls import *
# import os
import subprocess


if "_model" in locals() or "_model" in globals():
    pass
else:
    _model = fasttext.load_model("model_senti_v5.bin")

def get_sentiment(text):
    
    result = _model.predict(text)
    
    sentiment = result[0][0]
    confidence = result[1][0]
    if sentiment == '__label__1': ## Negative Sentiment
        senti = 'n'
    elif sentiment == '__label__2': ## Postive Sentiment
        senti = 'p'
    else:
        senti = 'u'
    return senti, confidence

# Create your views here.
def addSentenceView(request):
    x = request.POST['content']
    if x is '':
        return HttpResponseRedirect('/sentiment/')
    senti, confi = get_sentiment(x)
    confi = "%.2f" % confi
    new_sentence = SentimentTexts(sentence = x, detected_sentiment=senti, confidence=confi)
    new_sentence.save()
    return HttpResponseRedirect('/sentiment/')

def getsentenceView(request):
    all_sentences = SentimentTexts.objects.all().order_by('-id')[:20]
    return render(request, 'sentences.html', {'all_sentences':all_sentences })

def retrainView(request):
    retrain_sentences = SentimentTexts.objects.filter(retrain = True)
    f = open("sentiments.txt","a+")
    for sentence in retrain_sentences:
        if sentence.manual_sentiment == 'p':
            label = '__label__2'
        elif sentence.manual_sentiment == 'n':
            label = '__label__1'
        else:
            label = '__label__0'
        f.write("%s %s \r\n" % (label,sentence.sentence) )
    f.close() 
    retrain_sentences.update(retrain = False)
    subprocess.Popen(["python3","senti_retrain.py","-t"])
    return render(request, 'retrain.html')

def updatesentiView(request, i):
    sentence = SentimentTexts.objects.get(id= i)
    value = "senti" + str(i)
    x = request.POST[value]
    if sentence.manual_sentiment != x:
        sentence.manual_sentiment = x
        sentence.retrain = True
        sentence.save()
    return HttpResponseRedirect('/sentiment/')


    