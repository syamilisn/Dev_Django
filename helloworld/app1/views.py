from django.shortcuts import render, redirect
from . models import Intro
from . forms import IntroForm

def index(request):
    """index page"""
    intros = Intro.objects.order_by('id')
    context = {'intros':intros}
    return render(request, 'app1/index.html', context)

def input(request):
    """Take user input"""
    if request.method != 'POST':
        #no data submitted, return blank form
        form = IntroForm()
    else:
        #POST data is submittes, process data
        form = IntroForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('app1:index')
    #display blank or invalid form
    context = {'form':form}
    return render(request,'app1/input.html', context)

def edit(request, intro_id):
    """edit existing intro"""
    intro = Intro.objects.get(id=intro_id)
    if request.method !='POST':
        #initial req, prefill form with the current entry.
        form = IntroForm(instance=intro)
    else:
        #post data submittes' process data
        form = IntroForm(instance=intro,data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('app1:index')
    context = {'intro':intro,'form':form}
    return render(request,'app1/edit.html',context)