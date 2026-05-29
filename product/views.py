from django.shortcuts import render,redirect
from .models import Product
from django.contrib import messages

# Create your views here.
def create(request):
    if request.method=='GET':
        return render(request,'product/create.html')
    if request.method=='POST':
        pname = request.POST.get('pname')
        pprice = int(request.POST.get('pprice'))
        pcat = request.POST.get('pcat')

        pobj = Product.objects.create(pname=pname,pprice=pprice,pcategory=pcat)
        # products = Product.objects.all()
        messages.success(request, "Product Added successfully!")
        return redirect('view')
        # return render(request,'product/view.html',{'products':products,'msg':'Product inserted successfully'})

def view(request):
    if request.method=="GET":
        products = Product.objects.all()
        return render(request,'product/view.html',{'products':products})
    
def update(request,pk):
    if request.method=='GET':
        product = Product.objects.get(id=pk)
        return render(request,'product/update.html',{'product':product})
    if request.method=='POST':
        pname = request.POST.get('pname')
        pprice = float(request.POST.get('pprice'))
        pcat = request.POST.get('pcat')
        messages.success(request, "Product Updated successfully!")
        pobj = Product(id=pk,pname=pname,pprice=pprice,pcategory=pcat)
        pobj.save()
        return redirect('view')
    
def delete(request,pk):
    if request.method=='GET':
        product = Product.objects.get(id=pk)
        product.delete()
        # products = Product.objects.all()
        messages.success(request, "Product deleted successfully!")
        return redirect('view')
        # return render(request,'product/view.html',{'msg':'Product Deleted Successfullyy....','products':products})