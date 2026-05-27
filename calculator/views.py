from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def calculate(request):
    # print(request)
    # return HttpResponse('testing...')
    if request.method =='GET':
        return render(request,'calculator/index.html')
    if request.method=='POST':
        print(request.POST)
        v1 = int(request.POST['v1'])
        v2 = int(request.POST['v2'])
        operation=''
        if request.POST.get('add'):
            res = v1+v2
            operation='add'
        elif request.POST.get('subs'):
            res = v1-v2
            operation = 'subtraction'
        elif request.POST.get('multi'):
            res = v1*v2
            operation='multiplication'
        else:
            res = v1/v2
            operation='division'
        return render(request,'calculator/index.html',{'res':res,'operation':operation})
    

def mtable(request):
    if request.method=='GET':
        return render(request,'calculator/mtable.html')
    if request.method=='POST':
        v1 = int(request.POST['v1'])
        tables=[]
        for i in range(1,11):
            table = str(v1) + " * " + str(i) + " = " + str(v1*i)
            tables.append(table)
        # print(tables)
        return render(request,'calculator/mtable.html',{'tables':tables})
   