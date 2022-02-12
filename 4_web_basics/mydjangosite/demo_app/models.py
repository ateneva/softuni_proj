from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(
        max_length=50,
        null=True,
    )
    text = models.CharField(
        max_length=50
    )

    # return the task with their titles on the django admin page
    def __str__(self):
        return f'{self.id}: {self.title}'