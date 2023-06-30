from django.db import models
from django.utils.text import slugify
from froala_editor.fields import FroalaField


class Blog_Categories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True,blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Blog_Categories, self).save(*args, **kwargs)
    
    def count_categories(self):
        return Blog.objects.filter(__type = self.name).count()
    
    def __str__(self) -> str:
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    image = models.ImageField(upload_to='blog/')
    description = models.CharField(max_length=400)
    content = FroalaField()
    type = models.ManyToManyField(Blog_Categories)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']

    def save(self, *args, **kwargs):
     self.slug = slugify(self.title)
     super(Blog, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title