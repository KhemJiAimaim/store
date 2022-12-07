from django.shortcuts import render , get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from .models import Products , Category
from .forms import ProductForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

# Create your views here.


def index(request):
    category = Category.objects.all()
    product = Products.objects.filter()
    
    categ_id = request.GET.get('categoryid')
    if categ_id:
        #ถ้ามีค่า category
        product = product.filter(category_id=categ_id)

    paginator = Paginator(product,12)
    page = request.GET.get('page')
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)
    
    return render(request, 'store/index.html',{
        'product': product,
        'category': category,
        'categ_id' : categ_id,
    })


def product_add(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST , request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            form.save_m2m()
            messages.success(request, 'บันทึกสำเสร็จ')
            return HttpResponseRedirect(reverse('index' , kwargs={}))
        messages.error(request, 'บันทึกไม่สำเสร็จ!')
    return render(request, 'store/add.html' , {
        'form' : form , 
    })

def delete(request, id):
    product = Products.objects.get(id = id)
    product.delete()
    return HttpResponseRedirect(reverse('index'))
