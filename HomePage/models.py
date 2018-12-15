from django.db import models

class UserInfo(models.Model):
    your_name = models.CharField(max_length = 10)
    your_email = models.EmailField()
    your_password = models.CharField(max_length = 20)

    def __str__(self):
        return self.name_user
