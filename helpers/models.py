from django.db import models


# This class aims to track where and when models have been created

class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    # this code chunk aims to order the created models
    class Meta:
        abstract = True
        ordering = ('-created_at',)
