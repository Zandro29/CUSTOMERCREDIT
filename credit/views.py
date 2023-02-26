from django.shortcuts import render
from .models import Customer, Credit
from django.shortcuts import get_object_or_404, render
from .forms import CreditForm , CreateCreditForm
from django.contrib import messages

# Create your views here.

def all_credits(request):
    credit = Credit.objects.filter(is_active=True)
    return render(request, 'credits/home.html', {'credits': credit})
def credit_detail(request , id):
    credit = get_object_or_404(Credit, id=id, is_active=True)
    return render(request, 'credits/credit_detail.html', {'credit': credit})
def verify(request, id):
    data = Credit.objects.get(id=id)
    data.is_active = False
    data.save()
    credit = Credit.objects.filter(is_active=True)
    return render(request, 'credits/home.html', {'credits': credit})
def update_credit(request, id):
    obj= get_object_or_404(Credit, id=id)
        
    form = CreditForm(request.POST or None, instance= obj)
    context= {'form': form}
    if  request.method == "POST":
        if form.is_valid():
            obj= form.save(commit= False)

            obj.save()

            messages.success(request, "You successfully updated the post")

            context= {'form': form}

            return render(request, 'credits/update_credit.html', context)

        else:
            context= {'form': form,
                'error': 'The form was not updated successfully. Please enter in a title and content'}
            return render(request,'credits/update_credit.html' , context)
    return render(request,'credits/update_credit.html' , context = {'form': form})

def create_customer_credit(request):
    if  request.method == "POST":
        form = CreateCreditForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            credit = Credit.objects.filter(is_active=True)
            return render(request, 'credits/home.html', {'credits': credit})

    form = CreateCreditForm()
    context = {'form': form}
    return render(request, 'credits/create_credit.html', context)