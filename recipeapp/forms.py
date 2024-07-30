from django import forms
from .models import Recipe
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'image', 'description', 'ingredients', 'instructions', 'category']


    def clean(self):
        cleaned_data = super().clean()
        for field in ['name', 'description', 'ingredients', 'instructions', 'category']:
            if not cleaned_data.get(field):
                raise forms.ValidationError(f"{field} is required.")
        return cleaned_data
