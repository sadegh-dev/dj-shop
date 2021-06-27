from django.urls import path
from . import views

app_name = 'doshop'
urlpatterns = [  
    path('product/<slug:slug>/',views.product_detail, name='product-detail'),  
    path('category/<slug:slug>/',views.category_detail, name='category-detail'), 
    path('company/<slug:slug>/',views.company_detail, name='company-detail'), 
    path('special-price/',views.all_specialـprice, name='special-price'),
    path('page-not-found/',views.page_not_found, name='page_not_found'),
    #----- manager------------#
    path('insert-product/',views.insert_product, name='insert_product'),
    path('edit-product/<slug:slug>/',views.edit_product, name='edit_product'),
    path('edit-price-product/<slug:slug>/',views.edit_price_product, name='edit_price_product'),
    #------End manager -------#
    path('',views.home, name='home'),
    
]