from djongo import models


class Project(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000000)
    tags = models.CharField(max_length=1000000)
    url = models.CharField(max_length=1000)
    url_type = models.CharField(max_length=1000)
    secondary_url = models.CharField(max_length=1000)
    secondary_url_type = models.CharField(max_length=1000)
    order = models.CharField(max_length=100)

class Education(models.Model):
    title = models.CharField(max_length=1000)
    degree = models.CharField(max_length=1000)
    year = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000)
    order = models.CharField(max_length=100)

class Experience(models.Model):
    title = models.CharField(max_length=1000)
    company = models.CharField(max_length=1000)
    description = models.CharField(max_length=100000)
    year = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000)
    order = models.CharField(max_length=100)

class Research(models.Model):
    title = models.CharField(max_length=1000)
    conference = models.CharField(max_length=1000)
    description = models.CharField(max_length=100000)
    year = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000)
    order = models.CharField(max_length=100)

class Awards(models.Model):
    title = models.CharField(max_length=1000)
    competition = models.CharField(max_length=1000)
    description = models.CharField(max_length=100000)
    year = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000)
    order = models.CharField(max_length=100)