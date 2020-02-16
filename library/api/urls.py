from django.urls import path
from .views import *

urlpatterns =[
    path('customers/',view_get_post_customer),
    path('customers/<int:ID>',view_getByID_updateID_deleteByID),
]
