from django.db import models

class Customer(models.Model):
    fName = models.CharField(max_length=100)
    lName = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.fName} {self.lName}"
