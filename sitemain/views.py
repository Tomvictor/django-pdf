from django.shortcuts import render
from sitemain.models import BillBook
# Create your views here.
import datetime
from django.http import HttpResponse
from django.views.generic import View

from sitemain.utils import render_to_pdf #created in step 4

from django.template.loader import get_template

class GeneratePdf(View):
 def get(self, request, *args, **kwargs):
     template = get_template('invoice.html')
     context = {
         "invoice_id": 123,
         "customer_name": "John Cooper",
         "amount": 1399.99,
         "today": "Today",
     }
     html = template.render(context)
     pdf = render_to_pdf('invoice.html', context)
     if pdf:
         response = HttpResponse(pdf, content_type='application/pdf')
         filename = "Invoice_%s.pdf" %("12341231")
         content = "inline; filename='%s'" %(filename)
         download = request.GET.get("download")
         if download:
             content = "attachment; filename='%s'" %(filename)
         response['Content-Disposition'] = content
         return response
     return HttpResponse("Not found")




def home(request):
    context = {
        "objects":BillBook.objects.all()
        }
    return render(request,'home.html',context)

