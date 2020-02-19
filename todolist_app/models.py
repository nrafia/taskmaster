from django.db import models
from django.contrib.auth.models import User


class TaskList(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=250)
    task_detail = models.TextField(max_length=10000)
    done = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.task + " _ " + str(self.done) + " _ " + str(self.date_created) + " _ " + str(self.date_modified) + " _ " + str(self.owner.username)
