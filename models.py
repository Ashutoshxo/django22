from django.db import models


# Create your models here.
class music(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    genre = models.ForeignKey(music, on_delete=models.PROTECT)
    duration = models.PositiveIntegerField(help_text="Duration in seconds")
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/")
   

    def __str__(self):
        return str(self.title)


from django.contrib.auth.models import User


class cart(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE, db_column="uid")
    pid = models.ForeignKey(Song, on_delete=models.CASCADE, db_column="pid")
    qty = models.IntegerField(default=1)


# from.models import Breed
# admin.site.register(Breed)
