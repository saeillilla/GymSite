from django.db import models

from django.contrib.auth import get_user_model
from django.dispatch import receiver


# Create your models here.
class BMI(models.Model):
    userID: int
    age:int
    height:int
    weight:int
    BMI_value:int

class Subscription(models.Model):
    name = models.CharField(max_length=200,default='')
    pricing = models.CharField(max_length=200,default='')
    services = models.CharField(max_length=255)
    def __str__(self):
        return str(self.name)

class BMIData(models.Model):
    userID=models.IntegerField()
    age=models.IntegerField()
    height=models.IntegerField()
    weight=models.IntegerField()
    BMI=models.CharField(max_length=200)
    def __str__(self):
        return str(self.userID)

class Trainer(models.Model):
    name =models.CharField(max_length=200)
    field =models.CharField(max_length=200,default='')
    comments =models.CharField(max_length=200,default='')
    profile_pic = models.ImageField(upload_to ='static/img',default='')
    def __str__(self):
        return str(self.name)
    
class personToTrainer(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="user_likes")
    trainer = models.ForeignKey(Trainer,on_delete=models.CASCADE, related_name="post_likes")
    class Meta:
        unique_together = ["user", "trainer"]
    def __str__(self):
        return str(self.id)
class personToSubsc(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="subPerson")
    subscription = models.ForeignKey(Subscription,on_delete=models.CASCADE, related_name="subSub")
