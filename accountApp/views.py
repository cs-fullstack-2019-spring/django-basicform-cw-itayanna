from django.shortcuts import render
from django.http import HttpResponse
from .models import Account


# Create your views here.
def index(request):
    allAccounts = Account.objects.all()

    context = {
        'allAccounts': allAccounts
    }

    return render(request, 'accountApp/index.html', context)

def accountlogin(request):
    name = Account.name
    context = {
        'name': name
    }

    return render(request, 'accountapp/account.html', context)