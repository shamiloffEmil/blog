from django.contrib import admin
from .models import Post, Like, Dsc,Profile,Comment

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Dsc)
admin.site.register(Profile)