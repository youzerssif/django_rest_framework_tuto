from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    """Model definition for Category."""

    # TODO: Define fields here
    name = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name


class Post(models.Model):
    """Model definition for Post."""

    # TODO: Define fields here
    
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')
    
    options = (
        ('draft', 'Draft'),
        ('published','Published'),
    )
    
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    status = models.CharField(max_length=10, choices=options, default="published")
    objects = models.Manager() # default manager
    postobjects = PostObjects() # custum manager
    
    class Meta:
        """Meta definition for Post."""

        ordering = ('-published',)
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        """Unicode representation of Post."""
        return self.title
