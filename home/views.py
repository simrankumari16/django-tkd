from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact


# Create your views here.
def index(request):
    context={
        "variable1":"belief that you are worth defending."
    }
    return render(request,'index.html', context)
    #return HttpResponse("This is homepage")

def about(request):
     return render(request,'about.html')
    #return HttpResponse("This is about page")


def kick(request):
     return render(request,'kick.html')
    #return HttpResponse("This is about page")


def poomse(request):
     return render(request,'poomse.html')
     
def fight(request):
     return render(request,'fight.html')
def footer(request):
     return render(request,'footer.html')        

def services(request):
     return render(request,'services.html')


def contact(request):
     if request.method == "POST":
          
          name = request.POST.get('name')
          email = request.POST.get('email')
          phone = request.POST.get('phone')
          desc = request.POST.get('desc') 
          contact = Contact(name=name, email=email,phone=phone, desc=desc,date=datetime.today())


          contact.save()
     return render(request,'contact.html')      