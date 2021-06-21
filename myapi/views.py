from django.shortcuts import render, redirect
from .serializers import HeroSerializer
from rest_framework.generics import ListAPIView
from .models import Hero
from .forms import InputForm 
from datetime import datetime, date
from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        Form = InputForm(request.POST)
        if Form.is_valid():
            post = Form.save(commit=False)
            post.save()
            # return redirect('result')
            return HttpResponse("Data submitted successfully")
            # return redirect('index')

        else:
            return render(request, "index.html", {'form':Form}) 
    else:
        form = InputForm(None)
        return render(request, "index.html", {'form':form})
    
  
    

def result(request):
    date = ""
    month = ""
    year = ""
   
    if request.method == "POST":
      
        MyForm = InputForm(request.POST)
      
        if MyForm.is_valid():
            date = MyForm.cleaned_data['date']
            month = MyForm.cleaned_data['month']
            year = MyForm.cleaned_data['year']
            #MyForm.save()
            age = calc(date,month,year)
            my_obj = MyForm.save()
            my_obj.age = age
            my_obj.save()
        
        else:
            return render(request, "result.html", {'form':MyForm}) 

    else:
        MyForm = InputForm(None)
        
    context = {"date" : date, "month" : month, "year" : year,"age":age}
		
    return render(request, 'result.html',context )     

    

    
class viewApi(ListAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def calc(date,month,year):
    y = range(1,10)#if condition is to be put for 1-9 months otherwise error - time data '1952000' does not match format '%d %m %Y'
    
    if date in y:
        d1= '0'+str(date)
    else:
        d1=str(date)
    
    if month in y :
        m1='0'+ str(month)
    else:
        m1=str(month) 
    y1=str(year)
    s=d1+'/'+m1+'/'+y1
    date_of_birth = datetime.strptime(s, '%d/%m/%Y')
    age = calculate_age(date_of_birth)
    return age
