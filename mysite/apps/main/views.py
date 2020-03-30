from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .models import Answer, Value

def index(request):
    return render(request, 'main/index.html')

def task1(request):
    return render(request, 'main/task_1/task1.html')
def task2(request):
    return render(request, 'main/task_2/task2.html')
def task3(request):
    return render(request, 'main/task_3/task3.html')
def task4(request):
    return render(request, 'main/task_4/task4.html')
def task5(request):
    return render(request, 'main/task_5/task5.html')



def answer1(request):
    if request.POST:
        a = Answer(answer_text = request.POST.get('text'))
        a.save()
    return HttpResponseRedirect(redirect_to='../task_2/')
def answer2(request):
    if request.POST:
        a = Answer(answer_text = request.POST.get('text'))
        a.save()
    return HttpResponseRedirect(redirect_to='../task_3/')
def answer3(request):
    if request.POST:
        a = Answer(answer_text = request.POST.get('text'))
        a.save()
    return HttpResponseRedirect(redirect_to='../task_4/')
def answer4(request):
    if request.POST:
        a = Answer(answer_text = request.POST.get('text'))
        a.save()
    return HttpResponseRedirect(redirect_to='../task_5/')
def answer5(request):
    if request.POST:
        a = Answer(answer_text = request.POST.get('text'))
        a.save()
    return HttpResponseRedirect(redirect_to='../final/')
def value(request):
    if request.POST:
        v = Value(value = request.POST.get('range'))
        v.save()
    return HttpResponseRedirect(redirect_to='../info_5/')



def info1(request):
    return render(request, 'main/task_1/info1.html')
def info2(request):
    return render(request, 'main/task_2/info2.html')
def info3(request):
    return render(request, 'main/task_3/info3.html')
def info4(request):
    return render(request, 'main/task_4/info4.html')
def info5(request):
    return render(request, 'main/task_5/info5.html')

def final(request):
    return render(request, 'main/final/final.html')
