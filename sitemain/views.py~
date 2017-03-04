from django.shortcuts import render
from models import BillBook
# Create your views here.


def home(request):
    context = {
        "objects":BillBook.object.all()
        }
    return render(request,'home.html',context)
