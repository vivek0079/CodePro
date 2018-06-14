from django.db import models

from authenticate.models import User

# Create your models here.
class Code(models.Model):
    id              = models.CharField(max_length=10, null=False, blank=False, unique=True, primary_key=True)
    name            = models.CharField(max_length=30, null=False, blank=False)
    content         = models.TextField(null=False, blank=False)
    language        = models.CharField(max_length=20, null=False, blank=False)
    input           = models.TextField(null=False, blank=False)
    owner           = models.CharField(max_length=15, null=False, blank=False)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Code List'
        verbose_name_plural = 'Code List'
        ordering = ['timestamp']