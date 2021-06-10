from django import forms
from django.forms import fields
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm) :
    password1 = forms.CharField(
        label = 'رمز عبور',
        widget = forms.PasswordInput
    )
    password2 = forms.CharField(
        label = 'تکرار - رمز عبور',
        widget = forms.PasswordInput
    )
    class Meta :
        model = User
        fields = ('email','full_name')

    def clean_password2(self):
        p1 = self.cleaned_data['password1']
        p2 = self.cleaned_data['password2']
        if p1 and p2 and p1 != p2 :
            raise forms.ValidationError(' رمز عبور هم خوانی ندارند ')
        return p1

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit :
            user.save()
        return user



class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email','password','full_name')

    def clean_password(self):
        return self.initial['password']

