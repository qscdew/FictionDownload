from django.db import models
from django.contrib.auth.models import User

class Writer(models.Model):
    #作家
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(User,default='')
    def __str__(self):
        return self.name
        
class Bookinfo(models.Model):
    #每本书的详细信息
    name = models.CharField(max_length=30)
    writer = models.ForeignKey(Writer)
    jianjie =  models.TextField(max_length=600) #书的简介
    downurl = models.CharField(max_length=50)
    owner = models.ForeignKey(User,default='')
    xzl=models.IntegerField(default=0)
    length=models.IntegerField(default=0)
    def __str__(self):
        return self.name
        
        
class siteinfo(models.Model):
    fangwenliang=models.IntegerField(default=0)
    def __str__(self):
        return str(self.fangwenliang)
        
class Liuyan(models.Model):
    neirong= models.TextField(max_length=135)
    owner = models.ForeignKey(User)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.neirong  
    