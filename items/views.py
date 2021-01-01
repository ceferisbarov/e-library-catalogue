from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect  
from items.forms import ItemForm  
from items.models import Item

def item(request):  
    if request.method == "POST":
        form = ItemForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/items/show')
            except Exception as e: print(e)
    else:  
        form = ItemForm()  
    return render(request,'index.html',{'form':form})
	
def show(request):  
    items = Item.objects.all()  
    return render(request,"show.html",{'items':items}) 
  
class itemUpdateView(UpdateView): 
    # specify the model you want to use 
    model = Item
  
    # specify the fields 
    fields = ['etype', 'etitle', 'eauthor', 'estatus']
  
    # can specify success url 
    # url to redirect after successfully 
    # updating details 
    success_url ="/items/show"
'''	
def destroy(request, id):  
    item = Item.objects.get(id=id)
    item.delete()
    return redirect("/items/show")
'''