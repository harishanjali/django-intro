from django.shortcuts import render,redirect
from .models import Products,Categories
from django.contrib import messages
from .forms import InsertProduct
from django.shortcuts import render, get_object_or_404, redirect

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
    # Fetch the existing instance from the database
    instance = get_object_or_404(Products, pk=pk)

    if request.method == 'POST':
        # Bind the POST data AND the specific instance to the form
        form = InsertProduct(request.POST, request.FILES, instance=instance)
        
        if form.is_valid():
            form.save() # Automatically updates the existing instance
            return redirect('view') # Replace with your success URL
    else:
        # Pre-fill the form with the existing data for GET requests
        form = InsertProduct(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'product/model_form_insert.html', context)
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
        data_form = InsertProduct(request.POST,request.FILES)
        if data_form.is_valid():
            data_form.save()
            return redirect('view')
        else:
            return render(request,'product/model_form_insert.html')