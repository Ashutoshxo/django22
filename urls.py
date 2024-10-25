from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path("", views.show, name="index"),
    path("cat/<int:id>/", views.music_view, name="cat"),
    path("aaa/<int:id>/", views.aaa, name="aaa"),
    path("addsongit/", views.addsong),
    path("register/", views.register, name="register"),
    path("addsongs", views.addsongsview, name="addsongs"),
    path("logindetails", views.logindetails, name="logindetails"),
    path("logout", views.signout, name="logout"),
    path("searchmusic", views.searchview, name="searchmusic"),
    path("addtocart/<int:id>/", views.addtocart, name="addtocart"),
    path("addprod/<int:id>/", views.addprod, name="addprod"),
    path("viewcart/", views.viewcart, name="viewcart"),
    path("removesong/<int:id>/", views.removesong, name="removesong"),
]
