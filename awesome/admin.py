from django.contrib import admin
from .models import *

# Recommend List (Post)
admin.site.register(Post)

# Explore Awesome Stuffs
admin.site.register(Tag)
admin.site.register(Application)
