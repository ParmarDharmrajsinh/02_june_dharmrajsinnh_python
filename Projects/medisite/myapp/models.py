from django.db import models

# Create your models here.
class Medication(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField()

    from django.db import models

class Medication(models.Model):
    name = models.CharField(max_length=100)
    stock = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


