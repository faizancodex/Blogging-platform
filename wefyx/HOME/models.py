from django.db import models
from autoslug import AutoSlugField
from django.utils import timezone
from tinymce.models import HTMLField
from django.conf import settings 


# -------- CATEGORY MODEL --------
class Category(models.Model):
    cat_name = models.CharField(max_length=100, unique=True)
    cat_slug = AutoSlugField(populate_from="cat_name", unique=True)

    def __str__(self):
        return self.cat_name
    
# -------- POST MODEL --------
class Post(models.Model):  # Renamed from PostList
    post_category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts'
    )
    
    post_title = models.CharField(max_length=150)
    description = HTMLField()  # This will render TinyMCE in Django admin
    image = models.ImageField(upload_to='blog_images/')
    read_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)      #published 
    post_slug = AutoSlugField(populate_from="post_title", unique=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)

    

    @property
    def time_since_posted(self):
        now = timezone.now()
        diff = now - self.created_at

        seconds = diff.total_seconds()
        minutes = int(seconds // 60)
        hours = int(minutes // 60)
        days = diff.days
        weeks = days // 7
        months = days // 30
        years = days // 365

        if seconds < 60:
            return "just now"
        elif minutes < 60:
            return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
        elif hours < 24:
            return f"{hours} hour{'s' if hours != 1 else ''} ago"
        elif days < 7:
            return f"{days} day{'s' if days != 1 else ''} ago"
        elif weeks < 5:
            return f"{weeks} week{'s' if weeks != 1 else ''} ago"
        elif months < 12:
            return f"{months} month{'s' if months != 1 else ''} ago"
        else:
            return f"{years} year{'s' if years != 1 else ''} ago"

    def __str__(self):
        return self.post_title

    class Meta:
        ordering = ['-created_at']  # Default ordering: newest posts first
