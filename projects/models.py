from django.db import models
import uuid
    


class Project(models.Model):
    title = models.CharField(max_length=125)
    description = models.TextField(null=True, blank=True)  #null is for database ( allow to insert record without data in description field), #blank is for Django to know in forms that with POST request is allowed to get the empty values here
    featured_image = models.ImageField(blank=True, null=True, default='default.png')
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)  #'' are added becouse class Tag is declared below. If it would be above it's not necessary
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)
    
    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    # owner
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(unique=True, editable=False, 
                          default=uuid.uuid4, primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.value
    

class Tag(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          editable=False, primary_key=True)
    
    def __str__(self):
        return self.name


