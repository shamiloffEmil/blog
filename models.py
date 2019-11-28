from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE, )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Like(models.Model):
    post = models.ForeignKey('blog.Post', related_name='likes', on_delete=models.CASCADE, )
    like = models.PositiveIntegerField(validators=[MaxValueValidator(100)])

    def __strl__(self):
        return self.like

class Dsc(models.Model):
     post = models.ForeignKey('blog.Post', related_name='dscs',on_delete=models.CASCADE,)
     name = models.CharField(max_length=200)
     fio = models.CharField(max_length=200)
     age = models.IntegerField()
     city=models.CharField(max_length=200)
     inter=models.CharField(max_length=300)


     def __str__(self):
         return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    city = models.CharField(max_length=200)
    inter = models.CharField(max_length=300)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
#
# def update_profile(request, user_id):
#     user = Profile.objects.get(pk=user_id)
#     user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
#     user.save()