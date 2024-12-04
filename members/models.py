from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    membership_type = models.CharField(max_length=20, choices=[
        ('REGULAR', 'Regular'),
        ('PREMIUM', 'Premium'),
        ('VIP', 'VIP'),
    ])
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username