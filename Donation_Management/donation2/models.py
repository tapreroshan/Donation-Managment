# users/models.py
from django.contrib.auth.models import AbstractUser, User
from django.db import models

class UserProfile(models.Model):
    USER_TYPE_CHOICES = [
        ('donor', 'Donor'),
        ('receiver', 'Receiver'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Donation(models.Model):
    donor = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='donations')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='donations')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donor.user.username} donated to {self.post.title}"
