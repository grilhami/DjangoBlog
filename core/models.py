from __future__ import unicode_literals

from django.db import models

class TimestampedModel(models.Model):

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=False)

    class Meta:

        abstract = True
        ordering = ['-created', 'updated']
