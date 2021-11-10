from django.http import HttpResponse
from django.shortcuts import render

a=55
def home(request):
    return render(request,'home.html')
def count(request):
    fulltext=request.GET['fulltext']
    print(fulltext)
    s=1
    for i in fulltext:
        if i==" ":
            s+=1

    return render(request ,'count.html',{"fulltext":fulltext,"nbr":s})
def about(request):
    return render(request,'about.html',{"a":a})
