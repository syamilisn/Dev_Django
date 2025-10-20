from urllib import response
from django.shortcuts import render
def index(request):
    return render(request, 'app1/index.html')

import csv
from .models import Member
from django.http import HttpResponse
import datetime
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def export(request):
    response = HttpResponse(content_type = 'text/csv')
    writer = csv.writer(response)
    writer.writerow(['First name','Last name','Email','IP Address'])
    for member in Member.objects.all().values_list('first_name','last_name','email','ip_address'):
        writer.writerow(member)
    response['Content-Disposition'] = 'attachment; filename="members.csv"'
    return response

from django.http import HttpResponseRedirect
from .forms import UploadFileForm
# Imaginary function to handle an uploaded file.
from . handle_uploaded_file import handle_uploaded_file

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'app1/upload.html', {'form': form})

