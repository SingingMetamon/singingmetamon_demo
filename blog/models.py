from django.conf import settings
from django.db import models
from django.utils import timezone

class User_origin(models.Model):
    name = models.CharField(max_length=200)
    audio = models.FileField(upload_to="")

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.name

class Singer_origin(models.Model):
    name = models.CharField(max_length=200)
    audio = models.FileField(upload_to="")

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.name

class User_modified(models.Model):
    name = models.CharField(max_length=200)
    audio = models.FileField(upload_to="")

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.name