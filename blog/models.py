from django.db import models
from datetime import date
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photo/%y%m%d')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(null=False, blank=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body

