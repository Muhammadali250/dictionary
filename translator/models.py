from django.db import models

# Create your models here.
class Lugat(models.Model):

    inglizcha = models.CharField('English',max_length=256)
    uzbekcha = models.CharField("O'zbekcha" , max_length=256)
