from django.contrib import admin
from .models import Feed,User,Comment

admin.site.register(User)
admin.site.register(Feed)
admin.site.register(Comment)
# Register your models here.
