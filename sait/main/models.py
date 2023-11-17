from django.contrib.auth.models import User
from django.db import models


class ItemList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title


class ToDoItem(models.Model):
    to_do_list_item = models.ForeignKey(ItemList, on_delete=models.CASCADE)
    content = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.to_do_list_item.title