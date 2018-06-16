from django.db import models


class User(models.Model):
    username    = models.CharField(max_length=15, null=False, blank=False, unique=True)
    email       = models.URLField()
    password    = models.CharField(max_length=500, null=False, blank=False)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'User Objects'
        verbose_name_plural = 'User Objects'

    
