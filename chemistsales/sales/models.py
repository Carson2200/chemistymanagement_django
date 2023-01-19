from django.db import models


class Medicine(models.Model):
    objects = models.manager
    drugName = models.CharField(max_length=250)
    amount = models.CharField(max_length=5)
    clientName = models.CharField(max_length=250)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)

    userName = models.CharField(max_length=20)

    def __str__(self):
        return f'Medicine({self.drugName}, {self.clientName}, {self.email},{self.userName}, {self.phone})'
