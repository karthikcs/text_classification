from django import forms

class SentenceForm(forms.Form):
    sentence = forms.TextField(required=True, label='Sentence') 
    