from django.db import models
from users.models import CustomUser
# Create your models here.
class Guess(models.Model):
    sender=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content=models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.sender}: {self.content}'