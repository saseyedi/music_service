from django.contrib import admin

# Register your models here.
from api.music.models import Songs

admin.site.register(Songs)