from django.urls import path #this command says to import path
from . import views #for importing from views.py

urlpatterns=[
    path('',views.product_list,name='product_list'),
]