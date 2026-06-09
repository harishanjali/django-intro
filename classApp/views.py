from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from .forms import AddForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView
from product.models import Products

# Create your views here.
class Calculator(View):
    def get(self,request):
        emptyForm = AddForm()
        return render(request,'classApp/add.html',{'form':emptyForm})
    def post(self,request):
        emptyForm = AddForm()
        data = AddForm(request.POST)
        if data.is_valid():
            res = sum(data.cleaned_data.values())
            return render(request,'classApp/add.html',{'form':emptyForm,'result':res})
        else:
            return render(request,'classApp/add.html',{'form':data})
        
class InsertView(CreateView):
    model = Products
    fields = '__all__'
    template_name = 'classApp/insert.html'
    success_url = reverse_lazy('view')


class ModifyView(UpdateView):
    model = Products
    fields = '__all__'
    template_name = 'classApp/update.html'
    success_url = reverse_lazy('view')

class SeeListView(ListView):
    model = Products
    #to access the data in template we can give name
    context_object_name = 'products'
    template_name = 'classApp/view.html'

class MyDeleteView(DeleteView):
    model = Products
    template_name = 'classApp/delete.html'
    success_url = reverse_lazy('products-list')