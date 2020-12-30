from django.shortcuts import render, redirect  
from items.forms import ItemForm  
from items.models import Item

def item(request):  
    if request.method == "POST":
        form = ItemForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = ItemForm()  
    return render(request,'index.html',{'form':form})
	
def show(request):  
    items = Item.objects.all()  
    return render(request,"show.html",{'items':items}) 
	
def edit(request, id):  
    item = Item.objects.get(id=id)  
    return render(request,'edit.html', {'item':item})
	
def update(request, id):  
    item = Item.objects.get(id=id)  
    form = ItemForm(request.POST, instance = item)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'item': item})  
	
def destroy(request, id):  
    item = Item.objects.get(id=id)  
    item.delete()  
    return redirect("/show")