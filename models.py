
# Create your models here.
from django.db import models

class Feedback(models.Model):
    std_name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    rating = models.IntegerField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.std_name
