from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('new',views.new,name='new'),
    path('search',views.search,name='search'),
    path('add',views.add,name='add'),
    path('cart',views.cart,name='cart'),
    path('cont',views.cont,name = 'cont'),
    

]