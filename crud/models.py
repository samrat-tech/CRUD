from django.db import models

# Create your models here.


class Details(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=64, null=True, default="none")
    age = models.IntegerField()

    class Meta:
        verbose_name_plural = "Details"