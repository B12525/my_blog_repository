from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField()
    title_text = models.TextField()
    date = DateTimeField()

    def __str__(self):
        return self.title
