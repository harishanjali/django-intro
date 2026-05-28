from django.shortcuts import render

# Create your views here.

def students_app(request):
    return render(request,'students/main.html/')

def students_about(request):
    return render(request,'students/about.html/')