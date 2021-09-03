from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

RATING = [tuple([x,x]) for x in range(1,6)]

class Creeper(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(default='')
    survivability= models.IntegerField(default='1', choices=RATING)
    added = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('creeper_detail', args=[str(self.id)])
