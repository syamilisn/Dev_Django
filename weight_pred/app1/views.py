import csv
from django.shortcuts import render,redirect
from django.http import HttpResponse

from app1.models import Measure
from .forms import MeasureForm
def index(request):
    measures = Measure.objects.order_by('id')
    context = {'measures':measures}
    return render(request, 'app1/index.html',context)
    #return HttpResponse('Hello world')

def input(request):
    """Take user input"""
    if request.method != 'POST':
        #no data submitted, return blank form
        form = MeasureForm()
    else:
        #POST data is submittes, process data
        form = MeasureForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('app1:index')
    #display blank or invalid form
    context = {'form':form}
    return render(request,'app1/input.html', context)

def export(request):
    response = HttpResponse(content_type = 'text/csv')
    writer = csv.writer(response)
    writer.writerow(['weight','waist','hip','bust','arms','thigh','bottom','date'])
    for row in Measure.objects.all().values_list('weight','waist','hip','bust','arms','thigh','bottom','date'):
        writer.writerow(row)
    response['Content-Disposition'] = 'attachment; filename="measurements.csv"'
    return response
