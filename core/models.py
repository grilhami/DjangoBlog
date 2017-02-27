from __future__ import unicode_literals

from django.db import models

class TimestampedModel(models.Model):

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:

        abstract = True
        ordering = ['-created', '-updated']
