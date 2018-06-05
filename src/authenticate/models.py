from django.db import models

import ast
import base64

class ListField(models.TextField): #Custom ListField for Django .Ref: Django Docs
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return str(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

class User(models.Model):
    username    = models.CharField(max_length=15, null=False, blank=False, unique=True)
    email       = models.URLField()
    password    = models.CharField(max_length=20, null=False, blank=False)
    code_ids    = ListField()
    code_title  = ListField()
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.username)

    def __unicode__(self):
        return self(self.username)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'User Objects'
        verbose_name_plural = 'User Objects'

    
