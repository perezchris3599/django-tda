from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.Charfield(max_length=80)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
