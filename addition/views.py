from django.shortcuts import render
from .forms import Addition
from django.http import HttpResponse

# Create your views here.
def addition(request):
    if request.method=='GET':
        formAddition = Addition()
        print("in get request")
        return render(request,'addition/addition.html',{'form':formAddition})
    if request.method=='POST':
        print("in post")
        form_data = Addition(request.POST)
        print("below post")
        if form_data.is_valid() == True:
            print(form_data.cleaned_data)#contains the form data after success validation done by djnago behind
            return HttpResponse('Form submit success')
        else:
            print("in the else block")
            return render(request,'addition/addition.html',{'form':form_data})