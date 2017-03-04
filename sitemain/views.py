from django.shortcuts import render
from sitemain.models import BillBook
# Create your views here.


def home(request):
    context = {
        "objects":BillBook.object.all()
        }
    return render(request,'home.html',context)
