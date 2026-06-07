from django.shortcuts import render,redirect
from .models import Products,Categories
from django.contrib import messages
from .forms import InsertProduct

# Create your views here.
def create(request):
    if request.method=='GET':
        all_categories = Categories.objects.all()
        product = Products.objects.all()
        return render(request,'product/create.html',{'product':product,'categories':all_categories})
    if request.method=='POST':
        pname = request.POST.get('pname')
        pprice = float(request.POST.get('pprice'))
        cat = int(request.POST.get('pcat'))

        pobj = Products.objects.create(pname=pname,pprice=pprice,cat_id=cat)
        # products = Product.objects.all()
        messages.success(request, "Product Added successfully!")
        return redirect('view')
        # return render(request,'product/view.html',{'products':products,'msg':'Product inserted successfully'})

def view(request):
    if request.method=="GET":
        products = Products.objects.select_related('cat')
        return render(request,'product/view.html',{'products':products})
    
def update(request,pk):
    if request.method=='GET':
        product = Products.objects.get(id=pk)
        categories = Categories.objects.all()
        return render(request,'product/update.html',{'product':product,'categories':categories})
    if request.method=='POST':
        pname = request.POST.get('pname')
        pprice = float(request.POST.get('pprice'))
        pcat = request.POST.get('pcat')
        messages.success(request, "Product Updated successfully!")
        pobj = Products(id=pk,pname=pname,pprice=pprice,cat_id=pcat)
        pobj.save()
        return redirect('view')
    
def delete(request,pk):
    if request.method=='GET':
        product = Products.objects.get(id=pk)
        product.delete()
        # products = Product.objects.all()
        messages.success(request, "Product deleted successfully!")
        return redirect('view')
        # return render(request,'product/view.html',{'msg':'Product Deleted Successfullyy....','products':products})


def insert_product_form(request):
    if request.method=='GET':
        emptyform = InsertProduct()
        return render(request,'product/model_form_insert.html',{'form':emptyform})
        
    if request.method=='POST':
        data_form = InsertProduct(request.POST)
        if data_form.is_valid():
            data_form.save()
            return redirect('view')
        else:
            return render(request,'product/model_form_insert.html')