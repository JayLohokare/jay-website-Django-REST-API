from djongo import models


class Project(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000000)
    tags = models.CharField(max_length=1000000)
    url = models.CharField(max_length=1000)
    url_type = models.CharField(max_length=1000)
    secondary_url = models.CharField(max_length=1000)
    secondary_url_type = models.CharField(max_length=1000)