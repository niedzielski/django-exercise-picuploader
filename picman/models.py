from django.db import models
from django.forms import ModelForm

# Create your models here.
class Pic(models.Model):
    img = models.ImageField(upload_to='uploads/')
    def __unicode__(self):
        return self.img.path

class PicForm(ModelForm):
    class Meta:
        model = Pic
