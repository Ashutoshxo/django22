from django.shortcuts import render, HttpResponse, redirect
from .models import music, Song, cart
from .forms import registerform, addsongform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import addsongs, Userauthticationform


# Create your views here.


def register(request):
    if request.method == "POST":
        fm = registerform(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponse("I love Music")
    else:
        fm = registerform()
        return render(request, "register.html", {"form": fm})


def show(request):
    music1 = music.objects.all()
    song = Song.objects.all()
    context = {}
    context["music1"] = music1
    context["song"] = song

    return render(request, "index.html", context)


def music_view(request, id):

    song = Song.objects.filter(genre=id)
    music1 = music.objects.all()
    context = {}
    context["music1"] = music1
    context["song"] = song

    return render(request, "index.html", context)


def aaa(request, id):
    song = Song.objects.filter(genre=id)
    music1 = music.objects.all()
    context = {}
    context["music1"] = music1
    context["song"] = song
    return render(request, "desc.html", context)


def addsong(request):
    if request.method == "POST":
        fm = addsongform(request.POST)
        if fm.is_valid():

            return HttpResponse("data save")
    else:

        fm = addsongform()
        return render(request, "addsong.html", {"forms": fm})


def addsongsview(request):
    if request.method == "POST":
        fm = addsongs(request.POST, request.FILES)

        if fm.is_valid():
            fm.save()
            return HttpResponse("Data saved")

    else:
        fm = addsongs()
        return render(request, "addsongs.html", {"forms": fm})


from django.contrib.auth import authenticate, login, logout


def logindetails(request):
    if request.method == "POST":
        uname = request.POST["username"]
        upass = request.POST["password"]
        user = authenticate(request, username=uname, password=upass)
        if user is not None:
            login(request, user)
            return redirect("index")

    else:
        fm = Userauthticationform()
        return render(request, "logindetails.html", {"forms": fm})


def signout(request):
    logout(request)

    return redirect("index")


def searchview(request):
    if request.method == "POST":
        data = request.POST["search"]
        print(data)
        searchdata = Song.objects.filter(artist__icontains=data)
        return render(request, "search.html", {"searchdata": searchdata})
    else:
        return redirect("index")


from django.db.models import Q


def addtocart(request, id):
    if request.user.is_authenticated:
        userid = request.user.id
        # print(pid)
        u = User.objects.filter(id=userid)
        # print(u[0])
        p = Song.objects.filter(id=id)

        c = cart.objects.filter(Q(uid=u[0]) & Q(pid=p[0]))

        print(c)
        n = len(c)
        context = {}
        context = {"song": p}
        if n == 1:
            context["msg"] = "SONG is already in cart"
            return render(request, "viewsong.html", context)
        else:
            c = cart.objects.create(uid=u[0], pid=p[0])
            c.save()
            context["success"] = "song added to cart"
            return render(request, "viewsong.html", context)

    else:
        return redirect("logindetails")


# " return render(request, "addtocart.html")"


def addprod(request, id):
    song = Song.objects.filter(id=id)
    context = {"song": song}
    return render(request, "viewsong.html", context)


def viewcart(request):
    Userid = request.user.id
    print(Userid)
    data = cart.objects.filter(uid=Userid)
    context = {}
    context["data"] = data

    return render(request, "viewcart.html", context)


def removesong(request, id):
    c = cart.objects.filter(id=id)
    c.delete()

    return redirect("viewcart")
