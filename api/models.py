from __future__ import unicode_literals

from django.db import models


class Bucketlist(models.Model):
    """This class represent the bucketlist model"""
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        """Return a human readable representation of the model instance."""
        return self.name
