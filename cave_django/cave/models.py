from django.db import models

# Create your models here.
class User(models.Model):
    ussername = models.CharField(max_length=100, default="john12")
    first_name = models.CharField(max_length=100, default="john")
    last_name = models.CharField(max_length=100, default="str")

    def __str__(self):
        return self.ussername

class Comment(models.Model):
    comment = models.TextField(max_length=100, default="str")
    user = models.ForeignKey(
        to=User,
        on_delete = models.CASCADE,
        related_name = "comment",
        default=1
        )