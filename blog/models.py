from django.db.models import CharField
from django.urls import reverse
from django.utils import timezone
from django.db import models
# from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class PublishedManager(models.Manager):

    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ( 'draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique_for_date="publish ")
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)


    def __str__(self):
        return self.title

    objects = models.Manager()
    published = PublishedManager()


    # def get_absolute_url(self):
        # return reverse("")


post = Post.objects.filter(status='published')
p_posts = Post.published.all()







