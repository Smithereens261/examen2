from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    user_id = models.IntegerField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title