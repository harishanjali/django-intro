from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def calculate(request):
    print(request)
    # return HttpResponse('testing...')
    if request.method =='GET':
        return render(request,'index.html')
    if request.method=='POST':
        print(request.POST)
        v1 = int(request.POST['v1'])
        v2 = int(request.POST['v2'])
        res = v1+v2
        return HttpResponse(f'addition is ${res}')