from django.contrib import admin

# Register your models here.
from .models import music, Song, cart


class adminmusicmodel(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(music, adminmusicmodel)


class adminsong(admin.ModelAdmin):
    list_display = [
        "title",
        "artist",
        "album",
        "release_date",
        "genre",
        "duration",
        "created_at",
        "image",
    ]


admin.site.register(Song, adminsong)
admin.site.register(cart)
# admin.site.register(music)
# admin.site.register(Song)
