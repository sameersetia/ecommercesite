from django.shortcuts import render
from .models import Products, Order
from django.core.paginator import Paginator
# Create your views here.

def index(request):

    product_objects = Products.objects.all()

    category_name = request.GET.get('category')
    if category_name:
        product_objects = product_objects.filter(category__icontains=category_name)    
    #search
    item_name = request.GET.get('item_name')
    if item_name:
        product_objects = product_objects.filter(title__icontains=item_name)
    
    #paginator
    paginator = Paginator(product_objects, 8)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request,'shop/index.html',{'product_objects':product_objects})

def detail(request,id):
    product_object = Products.objects.get(id=id)
    return render(request, 'shop/detail.html',{'product_object':product_object})

def checkout(request):

    if request.method == "POST":
        items = request.POST.get('items',"")
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        contact_no = request.POST.get('contact_no',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        pin_code = request.POST.get('pin_code',"")
        total = request.POST.get('total',"")
        order = Order(items=items, name=name, email=email, contact_no=contact_no, address=address,
        city=city, state=state, pin_code=pin_code,total=total)
        order.save()
    return render(request,'shop/checkout.html')