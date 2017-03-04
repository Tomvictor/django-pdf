from django.shortcuts import render
from sitemain.models import BillBook
# Create your views here.


def home(request):
    context = {
        "objects":BillBook.objects.all()
        }
    return render(request,'home.html',context)


from django.http import HttpResponse
from django.views.generic import View

from sitemain.utils import render_to_pdf #created in step 4

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
         data = {
              'today': datetime.date.today(), 
              'amount': 39.99,
             'customer_name': 'Cooper Mann',
             'order_id': 1233434,
         }
         pdf = render_to_pdf('invoice.html', data)
         return HttpResponse(pdf, content_type='application/pdf')
