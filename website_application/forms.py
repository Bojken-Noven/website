from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="", max_length=64, widget=forms.TextInput(attrs={"class": "login-form-username", "placeholder": "Username", "autofocus": True}))
    password = forms.CharField(label="", max_length=64, widget=forms.PasswordInput(attrs={"class": "login-form-password", "placeholder": "Password"}))