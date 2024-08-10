from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    imageSrc = models.URLField(max_length=200, blank=True, null=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    githubUrl = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    imageSrc = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
