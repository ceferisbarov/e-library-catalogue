from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect  
from items.forms import ItemForm  
from items.models import Item

def show(request):
    items = Item.objects.all()
    return render(request,"show.html",{'items':items})

class itemCreateView(CreateView): 
    model = Item
	
    template_name_suffix = '_create'
	
    fields = ['etype', 'etitle', 'eauthor', 'estatus']
    success_url ="/items/show"
	  
class itemUpdateView(UpdateView): 
    model = Item
  
    fields = ['etype', 'etitle', 'eauthor', 'estatus']
  
    success_url ="/items/show"
	
class itemDeleteView(DeleteView):
    model = Item 
      
    success_url ="/items/show"