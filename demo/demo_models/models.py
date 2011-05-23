from django.db import models
from queryset_decorator import DecoratorManager

class Item(models.Model):
    path = models.CharField(max_length = 255)

    objects = DecoratorManager()

    def __unicode__(self):
        return self.path

    def get_absolute_url(self):
        return '/%s/' % self.path.strip('/')
