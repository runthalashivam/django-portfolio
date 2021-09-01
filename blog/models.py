from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    body = models.TextField()

    def __str__(self) -> str:
        return self.title
