from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

class Snack(models.Model):
    purchaser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        # return reverse('snack_list')
        return reverse('snack_detail',args=[str(self.id)])
        
    