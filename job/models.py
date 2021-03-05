from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

JOB_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
   )

def upload_image(instance,filename):
    image_name , extension = filename.split('.')
    return "jobs/%s.%s"%(instance.id,extension)

class Job(models.Model):

    title=models.CharField(max_length=50)
    owner=models.ForeignKey(User,related_name='job_owner',on_delete=models.CASCADE)
    #location
    job_type=models.CharField(max_length=20,choices=JOB_TYPE)
    description=models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True)
    image=models.ImageField(upload_to='jobs/')
    slug=models.SlugField(blank=True,null=True)
    
    def __str__(self):
        return self.title

    def save(self,*args,**wargs):
        self.slug=slugify(self.title)
        super(Job,self).save(*args,**wargs)
        
class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Apply(models.Model):
    job=models.ForeignKey(Job,related_name='apply_job',on_delete=models.CASCADE)        
    name=models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_now=True)
    email=models.EmailField(max_length=30)
    cv=models.FileField(upload_to='apply/')
    website=models.URLField()
    cover_letter=models.TextField(max_length=500)
    
    
    def __str__(self):
        return self.name



