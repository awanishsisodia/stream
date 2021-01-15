from django.contrib import admin
from .models import VideoData,Trending,Recently,Logo

# Register your models here.
admin.site.register(VideoData)
admin.site.register(Trending)
admin.site.register(Recently)
admin.site.register(Logo)
