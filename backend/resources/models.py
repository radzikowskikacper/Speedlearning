from django.db import models


class Resource(models.Model):
    name = models.CharField(max_length=200)
    type = models.IntegerField()  # 0 - PDF, 1 - code
