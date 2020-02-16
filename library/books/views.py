from django.shortcuts import render
from .models import *
from django.http import *
from .models import picture
from django.contrib.auth import authenticate
from django.template import Template,Context
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import Context
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    """View function for home page of site."""
    # # Generate counts of some of the main objects
    # num_browses = browse.objects.all().count()
    # num_instances = browseInstance.objects.all().count()
    # # Available copies of browses
    # num_instances_available = browseInstance.objects.filter(status__exact='a').count()
    # num_authors = Author.objects.count()  # The 'all()' is implied by default.

    # # Number of visits to this view, as counted in the session variable.
    # num_visits = request.session.get('num_visits', 0)
    # request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index/index.html'
    )

def book(request):
    #view function for browsing books
    browse_book= browse()
    return render(request,'book/browse.html',{browse_book:browse_book})
    
    #Upload Part
def upload(request):
     return render(request,'upload.html')

def upload_save(request):
    print("uploading ......]")
    p=request.FILES['image']
    from .models import picture
    user=picture(pic=p)
    user.save()
    return render(request, 'upload.html')

from django.shortcuts import render
from django.http import HttpResponse
from .models import *


#CRUD Part vIEW

def view_book(request):
    return render(request, 'book.html')

def view_bookdata_save(request):
    if request.method == "POST":
        get_all = request.POST
        print(get_all)
        get_Bookname = request.POST['book_bookname']
        get_Authorname= request.POST['book_author']
        get_Price = request.POST['book_price']
        get_Describe= request.POST['book_describe']
        book_obj = book(bookname=get_Bookname, author= get_Authorname,price=get_Price,
        describe =get_Describe)
        book_obj.save()
        return redirect(view_book)
    else:
        return render(request, "bookview.html")

# # for deleting 
#delete 
def view_book_delete(request,ID):  
    print(ID)
    book_obj = book.objects.get(id=ID)  
    context_variable={
        'book':book_obj
    }
    book_obj.delete()
    return render(request,'bookdelete.html',context_variable) 

    # for updating:
def view_book_update(request, ID):
    if request.method == "POST":
        get_all = request.POST
        print(get_all)
        get_Bookname = request.POST['book_bookname']
        get_Authorname= request.POST['book_author']
        get_Price = request.POST['book_price']
        get_Describe= request.POST['book_describe']
        book_obj = book(bookname=get_Bookname, author= get_Authorname,price=get_Price,
        describe =get_Describe )
        book_obj.save()
        return redirect(view_book_lists)
    else:
        print(ID)
        book_obj = book.objects.get(id=ID)  
        context_variable={
            'book':book_obj
        }
        return render(request,"bookupdate.html",context_variable) 

        def view_book_page(request):
            return render(request,'book.html')
#List OF BOOK DATA
def view_book_lists(request):
    list_of_book=book.objects.all()
    print(list_of_book)
    context_variable = {
        'book':list_of_book
    }
    return render(request,'bookview.html',context_variable)

    #Search function
def search(request):
    if request.method=="POST":
        srh= request.POST['sea']
    
        if srh:
            match = book.objects.filter(bookname__icontains=srh)

            if match:
                return render(request,'search.html', {"sr":match})
            else:
                return HttpResponse('Not successful')
        else:
            return('Not success')
    else:
        return render(request, 'search.html')

    #Customer
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import Template,Context
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import Context
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
    #create customer
def  view_customer(request):
    return render(request, 'customer.html')

def view_customerdata_save(request):
    if request.method == "POST":
        get_all = request.POST
        get_customerName = request.POST['customer_CustomerName']
        print(get_customerName)
        get_customerEmail = request.POST['customer_CustomerEmail']
        print(get_customerEmail)
        get_customerPhoneNo = request.POST['customer_CustomerPhoneNo']
        print(get_customerPhoneNo)
        get_customerAddress = request.POST['customer_CustomerAddress']
        print(get_customerAddress)
        customer_obj = customer(customerName=get_customerName, customerEmail=get_customerEmail,
        customerPhoneNo=get_customerPhoneNo, customerAddress=get_customerAddress)
        customer_obj.save()
        return HttpResponse("The data is saved in database")
    else:
         return HttpResponse("Error in saving")

         #delete CUSTOMER
def view_customer_delete(request,ID):  
    print(ID)
    customer_obj = customer.objects.get(id=ID)  
    context_variable={
        'customer':customer_obj
    }
    customer_obj.delete()
    return render(request,'customerdelete.html',context_variable) 

# for updating CUSTOMER DATA
def view_customer_update(request, ID):
    if request.method == "POST":
        get_all = request.POST
        print(get_all)
        get_customerName = request.POST['customer_CustomerName']
        get_customerEmail= request.POST['customer_CustomerEmail']
        get_customerPhoneNo = request.POST['customer_CustomerPhoneNo']
        get_customerAddress= request.POST['customer_CustomerAddress']
        customer_obj = customer(customerName=get_customerName, customerEmail=get_customerEmail,
        customerPhoneNo=get_customerPhoneNo, customerAddress=get_customerAddress)
        customer_obj.save()
        return redirect(view_customer_lists)
    else:
        print(ID)
        customer_obj = customer.objects.get(id=ID)  
        context_variable={
            'customer':customer_obj
        }
        return render(request,"customerupdate.html",context_variable) 

        def view_customer_page(request):
            return render(request,'customer.html')

            #List OF CUSTOMER DATA
def view_customer_lists(request):
    list_of_customer=customer.objects.all()
    print(list_of_customer)
    context_variable = {
        'customer':list_of_customer
    }
    return render(request,'customerview.html',context_variable)
  
  #image.html Part
def view_pic(request):
    users=picture.objects.all()
    p=users[len(users)-1].pic
    return render(request, 'image.html',{'users':users})