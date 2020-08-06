from django.http import HttpResponseRedirect, HttpResponse 
from django.shortcuts import render
from .forms import UploadFileForm, SingleTicketForm
import os
import time
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import fasttext

# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file

def handle_uploaded_file(f):
    with open('saptickets.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    os.system('python3 ../sap_ticket_cat.py -f saptickets.txt')


def upload_file(request):
    predicted = ''
    os.system('rm saptickets.txt*')
    time.sleep(1)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        desc_form = SingleTicketForm(request.POST)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            # return HttpResponseRedirect('success')
            time.sleep(3)
            file_path = 'saptickets.txt_labels.csv'
            if os.path.exists(file_path):
                # print('Inside download')
                with open(file_path, 'rb') as fh:
                    response = HttpResponse(fh.read(), content_type="text/csv")
                    response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
                    return response
            raise Http404    
        if desc_form.is_valid():
            desc = desc_form.cleaned_data['description']
            print('Description is ', desc)
            model = fasttext.load_model("../model_sap_ticket.bin")
            result=model.predict(desc, k=3)
            # print(result[0])
            predicted = result[0]
        
        # desc_form.data['description']  = ''

    else:
        form = UploadFileForm()
        desc_form = SingleTicketForm()
    return render(request, 'upload.html', {'form': form, 'desc_form': desc_form, 'predicted':predicted})

def success(request): 
    # return HttpResponse('Successfully uploaded')     
    time.sleep(2)
    return render(request, 'image_upload_success.html')

