from django import forms

class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField()

class SingleTicketForm(forms.Form):
    description = forms.CharField(label='Description', max_length=500, initial='')
    # predicted = forms.CharField(label='Predicted Categories: ', initial='', required=False)