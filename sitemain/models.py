from django.db import models

# Create your models here.


class BillBook(models.Model):
    title = models.CharField(max_length=100, default = "title")
