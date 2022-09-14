from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Brand, Category

from django.db.models import Q, F

from django.db.models.aggregates import Count, Min, Max, Sum, Avg


'''
def post_list(request):`
    products = prdoct.objects.all()
    category = Category.objects.all()
    return render(request, 'product.html',{})
    
    
    function :                      class
        - query                         - query
        -template                       - template  model_list  object_list
        -context                        - context   model_list  object_list

'''
def product_list(request):
    #products = Product.objects.all()
    #products = Product.objects.filter(price__range=(20,60))
    #products = Product.objects.filter(category__id__gte=6)
    
    #products = Product.objects.filter(name__endswith='on', quantity__gt=90)
    #products = Product.objects.filter(Q(name__endswith='on') |  ~Q(quantity__gt=90) )

    #products = Product.objects.filter(quantity= F('price'))
    
    #products = Product.objects.filter(price__range=(20,60)).order_by('price')
    #products = Product.objects.earliest('name')
    #products = Product.objects.latest('name')
    #products = Product.objects.all()[10:20]

    #products = Product.objects.values_list('name','price','category__name','brand__name')
    
    #products = Product.objects.only('name')
    #products = Product.objects.select_related('category').all()
  
    #products = Product.objects.select_related('category').select_related('brand').all()
    #one-to-one or one-to-many --> select related? many-to-many prefetch_related 
    
    products = Product.objects.aggregate(myavg = Avg('price'), mymax = Max('price'))
    
    return render(request, 'products/product_list_test.html',{'products':products})



class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product


class BrandList(ListView):
    model = Brand

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

    # class single : edit detail delete
class BrandDetail(DetailView):
    model = Brand

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.get_object()
        context["brand_products"] = Product.objects.filter(brand=brand)
        return context
    

class CategoryList(ListView):
    model = Category
    
