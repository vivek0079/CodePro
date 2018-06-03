from django.db import models

# Create your models here.
class Code(models.Model):
    id              = models.CharField(max_length=10, null=False, blank=False, unique=True, primary_key=True)
    content         = models.TextField(null=False, blank=False)
    language        = models.CharField(max_length=20, null=False, blank=False)
    input           = models.TextField(null=False, blank=False)
    compile_status  = models.CharField(max_length=50, null=False, blank=False)
    run_status      = models.CharField(max_length=50, null=False, blank=False)
    run_time        = models.CharField(max_length=10, null=False, blank=False)
    run_memory      = models.CharField(max_length=10, null=False, blank=False)
    output_html     = models.TextField(null=False, blank=False)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.id)
    
    def __unicode__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Code'
        verbose_name_plural = 'Codes'
        ordering = ['timestamp']