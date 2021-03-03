from django.db import models

# Create your models here.
class User(models.Model):
    ussername = models.CharField(max_length=100, default="john12")
    first_name = models.CharField(max_length=100, default="john")
    last_name = models.CharField(max_length=100, default="str")
    password = models.CharField(max_length=100, default="password")

    def __str__(self):
        return self.ussername

class Comment(models.Model):
    likes = models.IntegerField(default=0)
    comment = models.TextField(max_length=300, default="str")
    user = models.ForeignKey(
        to=User,
        on_delete = models.CASCADE,
        related_name = "comment",
        default=1
        )