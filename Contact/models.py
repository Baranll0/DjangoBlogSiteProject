from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30,verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    content = models.TextField(verbose_name="Message",max_length=250)
    def __str__(self):
        return self.name
