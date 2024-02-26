from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.
# Create your models here.
CHOICES = (
        ('inprogress', 'IN PROGRESS'),
        ('done', 'DONE'),
        ('to-do', 'TO-DO'),
    )


class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def profile(self):
        profile = Profile.objects.get(user=self)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=1000)
    bio = models.CharField(max_length=100)
    image = models.ImageField(upload_to="user_images", default="default.jpg")
    verified = models.BooleanField(default=False)
    def __str__(self):
        return self.full_name


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)

class TodoTask(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=50,null=True,blank=True)
    description = models.CharField(max_length=150,null=True,blank=True)
    dateandtime = models.DateTimeField(max_length=150,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,choices=CHOICES,blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
