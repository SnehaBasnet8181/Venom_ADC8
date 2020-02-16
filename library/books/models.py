from django.db import models

# Create your models here.

#UPLOAD PART
class picture(models.Model):
  pic= models.ImageField(upload_to="")

#BOOK PART
class book(models.Model):
   
    bookname = models.CharField(max_length=50)
    author=models.CharField(max_length=70)
    price = models.IntegerField()
    describe = models.CharField(max_length=400)
    
    
    
    def __str__(self):  
        return  self.bookname +""+ self.author +""+str(self.price)+""+ str(self.describe)
    
    # def is_valid_patient(self):

    #     return (self.bookname !=self.p) and (self.patientAge >=0)

    #CUSTOMER PART
class customer(models.Model):
  customerName = models.CharField(max_length=200)
  customerEmail = models.CharField(max_length=200)
  customerPhoneNo = models.IntegerField()
  customerAddress = models.CharField(max_length=200)