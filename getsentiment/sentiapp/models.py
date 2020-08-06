from django.db import models

# Create your models here.
class SentimentTexts(models.Model):
    sentence = models.TextField() 
    detected_sentiment = models.CharField(max_length=1) # p-> Pos n->Neg  u->Neutral
    confidence = models.FloatField(default = 0)
    manual_sentiment = models.CharField(max_length=1) # p-> Pos n->Neg  u->Neutral
    retrain = models.BooleanField(default = False)