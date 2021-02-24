from django.db import models

# Create your models here.
class User(models.Model):
    ussername = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.ussername

class Comment(models.Model):
    comment = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = "comment"
        )