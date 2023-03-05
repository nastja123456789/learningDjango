from django import forms
from django.contrib import admin
from .models import Comment, Recipe, Category, Product


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'img_url')


class SearchForm(forms.Form):
    query = forms.CharField()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )


class PredictForm(forms.Form):
    category = forms.CharField()
    price = forms.FloatField()