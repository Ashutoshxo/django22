from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Song


class addsongform(forms.Form):
    title = forms.CharField(max_length=100, label="Song Title")
    artist = forms.CharField(max_length=100, label="Artist")
    album = forms.CharField(max_length=100, label="Album", required=False)
    genre = forms.CharField(max_length=50, label="Genre", required=False)


class registerform(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

        labels = {
            "username": "Enter Username",
            "first_name": "Enter First name",
            "last_name": "Enter last name",
            "email": "enter email",
            "password1": "Enter PASSWORD",
        }

        username = forms.CharField(
            widget=forms.TextInput(attrs={"class": "form-control"})
        )
        first_name = forms.CharField(
            widget=forms.TextInput(attrs={"class": "form-control"})
        )
        last_name = forms.CharField(
            widget=forms.TextInput(attrs={"class": "form-control"})
        )
        email = forms.EmailField(
            widget=forms.EmailInput(attrs={"class": "form-control"})
        )
        password1 = forms.CharField(
            widget=forms.PasswordInput(attrs={"class": "form-control"})
        )


class addsongs(forms.ModelForm):
    class Meta:
        model = Song
        fields = [
            "title",
            "artist",
            "album",
            "release_date",
            "genre",
            "duration",
            "image",
        ]
        labels = {
            "title": "Enter title",
            "artist": "enter artist",
            "album": "Enetr album",
            "release_date": "ENTER DATE",
            "genre": "ENTER GENRE",
            "duration": "ENTER",
            "image": "PUT IMAGE",
        }
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Song Title"}),
            "artist": forms.TextInput(attrs={"placeholder": "Artist Name"}),
            "album": forms.TextInput(attrs={"placeholder": "Album Name"}),
            "release_date": forms.DateInput(attrs={"type": "date"}),
            "genre": forms.Select(attrs={"type": "date"}),
            "duration": forms.TimeInput(attrs={"placeholder": "Duration (HH:MM:SS)"}),
            "image": forms.ClearableFileInput(attrs={"accept": "image/*"}),
        }


class Userauthticationform(AuthenticationForm):
    username = (
        forms.CharField(
            label="ENTER USERNAME",
            widget=forms.TextInput(attrs={"class": "form-control"}),
        ),
    )
    password = (
        forms.CharField(
            label="ENTER PASSWORD",
            widget=forms.PasswordInput(attrs={"class": "form-control"}),
        ),
    )

    class Meta:
        model = User
        fields = ["username"]
