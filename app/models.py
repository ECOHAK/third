from django.db import models

# Create your models here.
class Address(models.Model):
    address = models.CharField(max_length=20)

    def __str__(self):
        return self.address

class House(models.Model):
    number = models.IntegerField()
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.number) + self.address.address   #out[]: 101부산시청  오버라이딩했어.
    #이걸 shell에 반영해야 오버라이드도 반영.