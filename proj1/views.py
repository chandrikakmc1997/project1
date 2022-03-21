import dataclasses
from django.http import HttpResponse


def home(request):
    print(request)
    return HttpResponse('hello world')

def welcome(request):
    data="""<!doctype html>
    <html>
    <head>
    <title>Welcome page</title>
    </head>
    <body>
    <h1>Welcome To django</h1>
    </body>    
    </html>"""
    return HttpResponse(data)
def index1(request):
    fp=open(r"C:\Users\CHANDRIKA\Desktop\Django\project1\proj1\welcome.html",'r')
    temp=fp.read()
    return HttpResponse(temp)
def web1(request):
    fp1=open(r'C:\Users\CHANDRIKA\Desktop\Django\project1\proj1\html\assignment1.html','r')
    temp1=fp1.read()
    return HttpResponse(temp1)

    

    
