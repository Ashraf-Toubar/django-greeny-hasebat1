from django.urls import path
from .views import ProductList, ProductDetail, BrandList, BrandDetail, CategoryList #, product_list
from .api import ProdcutList ,ProdcutDetail #, product_list_api, product_detail

app_name = 'products'


urlpatterns = [
    #path('testing/', product_list),
    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('brands/', BrandList.as_view(), name='brand_list'),
    path('brands/<int:pk>', BrandDetail.as_view(), name='brand_detail'),
    path('category/', CategoryList.as_view(), name='category_list'),



    # path('api/list' , product_list_api),
    # path('api/list/<int:id>' , product_detail),
    
    path('api/list/cbv' , ProdcutList.as_view()),
    path('api/list/cbv/<int:pk>' , ProdcutDetail.as_view()),
]
