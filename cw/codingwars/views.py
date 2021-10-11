from django.shortcuts import render, redirect
from .models import SubjectNames
from django.http import HttpResponse
from datetime import datetime
from time import sleep
from .models import *
from .forms import SubjectNamesForm, UrokiForm


# Create your views here.


def home(request):
    # return HttpResponse("Welcome to Coding Wars")
    return render(request, "codingwars/home.html")


def subject_names(request):
    lang = SubjectNames.objects.all()
    context = {
        "lang": lang,
    }
    return render(request, 'codingwars/subject_list.html', context)


def create_subject(request):
    error = ''
    if request.method == "POST":
        form = SubjectNamesForm(request.POST)
        if form.is_valid():
            form.save()
            # здесь по сути можно добавить строку сообщающей об успешном добавлении урока
            return redirect('subject_names')
        else:
            error = "Форма неверно заполнена"
    form = SubjectNamesForm()

    data = {
        "form": form
    }
    return render(request, 'codingwars/create_subject.html', data)


def delete_subject(request, subject_id):
    subject = SubjectNames.objects.get(pk=subject_id)
    subject.delete()
    return redirect('subject_names')


def main_page(request):
    return render(request, "codingwars/subject_list.html")


def watch_now(request):
    return render(request, "codingwars/time_now.html")


def uroki(request, subject_id):
    uroki = Uroki.objects.filter(subject_id=subject_id)
    data = {
        "uroki": uroki,
        "subject_id": subject_id,
    }
    return render(request, "codingwars/uroki.html", data)


def create_urok(request, subject_id):
    error = ''
    if request.method == "POST":
        form = UrokiForm(request.POST)
        if form.is_valid():
            form.save()
            # здесь по сути можно добавить строку сообщающей об успешном добавлении урока
            return redirect('subject_names')
        else:
            error = "Форма неверно заполнена"
    form = UrokiForm()

    data = {
        "form": form,
        "subject_id": subject_id,
    }
    return render(request, 'codingwars/create_urok.html', data)


def delete_urok(request, urok_id):
    urok = Uroki.objects.get(pk=urok_id)
    urok_name = urok.urok_name
    data={
        "urok_name": urok_name
    }
    urok.delete()
    # return redirect("subject_names")
    return render(request, "codingwars/deleted.html", data)