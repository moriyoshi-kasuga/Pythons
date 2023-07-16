from django.http import HttpResponse
from django.shortcuts import render


def taskList(request) -> None:
    return HttpResponse("To Do list")
