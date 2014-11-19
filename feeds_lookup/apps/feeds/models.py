from django.db import models


class Feed(models.Model):
    name = models.CharField(max_length=1024)
    url = models.URLField(null=True, blank=True)
    description = models.CharField(max_length=1024, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024, null=True, blank=True)

    def __unicode__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=1024, null=True)
    url = models.URLField()
    description = models.CharField(max_length=2048, null=True, blank=True)
    source = models.CharField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(editable=False, null=True, auto_now_add=True)
    feed = models.ForeignKey(Feed)
    tags = models.ManyToManyField(Tag, null=True, blank=True)

    def __unicode__(self):
        return self.title

