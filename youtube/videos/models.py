from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videos')

    file_id = models.CharField(max_length=255)
    video_url = models.URLField(max_length=500)
    thumbnail_url = models.URLField(max_length=500, blank=True)

    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def display_thumbnail_url(self):
        if self.thumbnail_url:
            return self.thumbnail_url
        # auto-generate thumbnail from ImageKit if none uploaded
        return f"{self.video_url}/ik-thumbnail.jpg"

    @property
    def streaming_url(self):
        return self.video_url 

    @property
    def optimized_url(self):
        # fallback direct video URL
        return self.video_url