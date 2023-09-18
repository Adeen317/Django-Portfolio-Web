from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from BASE import models
from BASE.models import Contact

def home(request):
    return render(request,'home.html')
def contact(request):
    if request.method=="POST":
        print('post')
        name=request.POST.get('name')
        email=request.POST.get('email')
        content=request.POST.get('content')
        number=request.POST.get('number')
        print(name,email,number,content)

        if len(name)>1 and len(name)<30:
            pass
        else:
            messages.error(request,'Length of name should be greater than 2 and less than 30 words')
            return render(request,'home.html')
        
        if len(email)>1 and len(email)<30:
            pass
        else:
            messages.error(request,'Invalid email try again')
            return render(request,'home.html')

        if len(number)>1 and len(number)<11:
            pass
        else:
            messages.error(request,'Invalid number try agan')
            return render(request,'home.html')

        ins=models.Contact(name=name,email=email,content=content,number=number)
        ins.save()
        message.success(request,'Thank You for Reaching me out||Your message has been saved')
        print('Data has been saved in the database')
        print('The request is no pass')

    return render(request,'home.html')
# Create your views here.
