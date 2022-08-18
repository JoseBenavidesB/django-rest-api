from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False , help_text='Title',verbose_name='title')
    description = models.CharField(max_length=600, null=False, help_text='Description', blank=False , verbose_name='description')
    image_url = models.URLField(blank=False)
    created_at = models.DateField(auto_now_add=True, verbose_name='created_at')
    updated_at = models.DateField(auto_now=True, verbose_name='created_at')

    
    def __str__ (self):
        return self.title