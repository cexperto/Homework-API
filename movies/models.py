from django.db import models
from customusers.models import CustomUser

PRIVATE_CHOICES = (
    (0,0), 
    (1,1),
    )
    

class Movies(models.Model):
    """
    private field choices:
    0 = public content
    1 = private content
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    year = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    private = models.IntegerField(choices=PRIVATE_CHOICES)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="movies")

    def __str__(self):
        return self.name



