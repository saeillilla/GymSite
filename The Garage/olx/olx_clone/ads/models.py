from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category
    
class Disctrict(models.Model):
    district = models.CharField(max_length=100)

    def __str__(self):
        return self.district
    

class Ad(models.Model):
    ad_title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo1 = models.ImageField(upload_to ='static/img')
    photo2 = models.ImageField(upload_to ='static/img', blank=True, null=True)
    photo3 = models.ImageField(upload_to ='static/img', blank=True, null=True)
    photo4 = models.ImageField(upload_to ='static/img', blank=True, null=True)
    address = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    district = models.ForeignKey(Disctrict, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    def __str__(self):
        return self.ad_title
    
class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=20, verbose_name="Vehicle Name")
    vehicle_model = models.CharField(max_length=20, verbose_name="Vehicle Model")
    vehicle_color = models.CharField(max_length=20, verbose_name="Vehicle Color")
    vehicle_mileage = models.IntegerField(verbose_name="Vehicle Mileage")
    price = models.IntegerField(verbose_name="Price")
    vehicle_number = models.CharField(max_length=20, verbose_name="Vehicle Number")
    vehicle_insurance = models.CharField(max_length=20, verbose_name="Vehicle Insurance")
    accident_record = models.CharField(max_length=20, verbose_name="Accident Record")
    vehicle_fine_record = models.CharField(max_length=20, verbose_name="Vehicle Fine Record")
    photo1 = models.ImageField(upload_to='static/img', verbose_name="Photo 1")
    photo2 = models.ImageField(upload_to='static/img', blank=True, null=True, verbose_name="Photo 2")
    photo3 = models.ImageField(upload_to='static/img', blank=True, null=True, verbose_name="Photo 3")
    photo4 = models.ImageField(upload_to='static/img', blank=True, null=True, verbose_name="Photo 4")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="User")

    def __str__(self):
        return f"{self.vehicle_name} - {self.vehicle_number}"
    

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    landMark = models.CharField(max_length=255,default="")
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

class VerifiedUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    paymentCompleted = models.BooleanField(default=False)
    orderCompleted = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user.username} - {self.vehicle.vehicle_number}"  
    


class ReportAds(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.username} - {self.ad.vehicle_number}"  
