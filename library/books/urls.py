from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf.urls.static import static
from . import views


urlpatterns = [
    #my paths
    path('',index,name='index'),
    path('',book,name='book'),
    path('image',view_pic),

    path('book/',view_book),
    path('book/save',view_bookdata_save),
    path('bookdata/',view_book_lists),
    path('bookdata/bookdelete/<int:ID>',view_book_delete),
    path('bookdata/bookupdate/<int:ID>',view_book_update),
    


    path('uploadFIle/',upload),
    path('uploadFIle/upload',upload_save),
    # path('browse/' , Books  ,name='browse.html'),
    path('customer/',view_customer),
    path('customer/save',view_customerdata_save),
    path('customerdata/',view_customer_lists),
    path('customerdata/customerdelete/<int:ID>',view_customer_delete),
    path('customerdata/customerupdate/<int:ID>',view_customer_update),

       path('signup/',view_register_user),
    path('logout/',view_logout),
    path('login',view_authenticate_user, name="login"),

] 