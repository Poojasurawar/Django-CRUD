from django.shortcuts import render,redirect
from myapp.models import Contact
from myapp.forms import ContactForm

# Create your views here.
def display(request):
    x=Contact.objects.all()
    a={
        'myappdata':x
    }
    return render(request,'display.html',a)

def add(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("display")
    else:
        form=ContactForm()    
        b={
            "form":form
        }
    return render(request,"add.html",b)
    
def update(request,pk):
    x=Contact.objects.get(pk=pk)
    if request.method=='POST':
        form=ContactForm(request.POST,instance=x)
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
        form=ContactForm(instance=x)
    return render(request,'add.html',{'form':form})

def delete(request,pk):
    x=Contact.objects.get(pk=pk)
    if request.method=="POST":
        x.delete()
        return redirect('display')
    return render(request,'delete.html',{'object':x})            