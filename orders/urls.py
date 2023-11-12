from django.urls import path
from . import views

urlpatterns = [

path('place_order/',views.place_order,name='place_order'),
path('payment/',views.payment,name='payment'),
path('order_complate',views.order_complate,name='order_complate'),

]

