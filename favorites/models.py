from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')  # Prevent duplicates

    def __str__(self):
        return f"{self.user.username} -> {self.post.title}"
