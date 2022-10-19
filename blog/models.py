# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    #Post is the name  of our model
    #models.Model means that the Post is a django model,
    # so Django knows that it should be saved in the database
    #Then we define our properties. to do that we need to define each of the field 
    #(is it a text? A number? A date? A relation to another object like a User)
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date= timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
    
    
