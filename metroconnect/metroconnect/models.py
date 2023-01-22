from django.db import models


class customer_reg(models.Model):
    name  = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phonenumber = models.CharField(max_length=150)
    gender=models.CharField(max_length=150)
    password = models.CharField(max_length=150)


class staff_reg(models.Model):
    name  = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phonenumber = models.CharField(max_length=150)
    gender=models.CharField(max_length=150)
    designation=models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    image = models.FileField(max_length=150)

class stations(models.Model):
    stationname = models.CharField(max_length=150)

class trains(models.Model):
    trainno=models.CharField(max_length=150)
    trainname=models.CharField(max_length=150)
    traintime=models.CharField(max_length=150)
    stationname = models.CharField(max_length=150)
    trainimage= models.FileField(max_length=150)

class routes(models.Model):
    trainname=models.CharField(max_length=150)
    startstation = models.CharField(max_length=150)
    endstation = models.CharField(max_length=150)
    distance =models.CharField(max_length=150)
    rate=models.CharField(max_length=150)

class offers(models.Model):
    eventname=models.CharField(max_length=150)
    offer=models.CharField(max_length=150)

class parkings(models.Model):
    stationname=models.CharField(max_length=150)
    slot=models.CharField(max_length=150)
    rate=models.CharField(max_length=150)

class complaints(models.Model):
    customerid=models.CharField(max_length=150)
    complainsubject=models.CharField(max_length=150)
    description=models.CharField(max_length=150)
    

class userrequest(models.Model):
    customerid=models.CharField(max_length=150)
    startstation=models.CharField(max_length=150)
    endstation=models.CharField(max_length=150)
    date=models.CharField(max_length=150)
    

class ticket(models.Model):
    customerid=models.CharField(max_length=150)
    startstation=models.CharField(max_length=150)
    endstation=models.CharField(max_length=150)
    date=models.CharField(max_length=150)
    distance=models.CharField(max_length=150)
    rate=models.CharField(max_length=150)
    trainno=models.CharField(max_length=150)
    sid=models.CharField(max_length=150)
    status=models.CharField(max_length=150)

    
class userpayment(models.Model):
    customerid=models.CharField(max_length=150)
    startstation=models.CharField(max_length=150)
    endstation=models.CharField(max_length=150)
    date=models.CharField(max_length=150)
    rate=models.CharField(max_length=150)
    trainno=models.CharField(max_length=150)
    cardname=models.CharField(max_length=150)
    cardnumber=models.CharField(max_length=150)
    cardtype=models.CharField(max_length=150)
    sid=models.CharField(max_length=150)
    
    
class userslotpayment(models.Model):
    customerid=models.CharField(max_length=150)
    startstation=models.CharField(max_length=150)
    endstation=models.CharField(max_length=150)
    date=models.CharField(max_length=150)
    rate=models.CharField(max_length=150)
    cardname=models.CharField(max_length=150)
    cardnumber=models.CharField(max_length=150)
    cardtype=models.CharField(max_length=150)
