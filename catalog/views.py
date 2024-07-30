from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import get_template
from django.template.response import TemplateResponse

# Create your views here.

from . import models
# from . import forms

def main(request):
    # templ = (settings.BASE_DIR / 'templates/head.html').read_text(encoding='utf-8')
    
    # return HttpResponse(templ)
    return render(request, 'head.html')
    
# def products(request):
    # html_dock = TemplateResponse(
        # request,
        # 'products.html',
        # {
            # 'products': models.Product.objects.all(),
        # },
    # )
    # return html_dock
def products(request):
    products_list = models.Product.objects.all()
    return render(request, 'products.html', {'products': products_list})
   
def calculator(request):
    ...