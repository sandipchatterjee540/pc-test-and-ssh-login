from django.shortcuts import render
from django.http import HttpResponse


def sandip(request):
    return HttpResponse("<h1>Sandip chatterjee</h1>")

def deep(request):
    s=1+2
    return HttpResponse("<h1>Deep Bhattacharya </h1>"+str( s))