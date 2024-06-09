from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_no = models.IntegerField(max_length=12)
    instrument_type = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name
