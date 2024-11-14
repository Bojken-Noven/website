from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="", max_length=64, widget=forms.TextInput(attrs={"class": "login-form-username", "placeholder": "Username", "autofocus": True, "autocomplete": "on"}))
    password = forms.CharField(label="", max_length=64, widget=forms.PasswordInput(attrs={"class": "login-form-password", "placeholder": "Password"}))

class MobileLoginForm(forms.Form):
    username = forms.CharField(label="", max_length=64, widget=forms.TextInput(attrs={"class": "mobile-login-form-username", "placeholder": "Username", "autofocus": True, "autocomplete": "on"}))
    password = forms.CharField(label="", max_length=64, widget=forms.PasswordInput(attrs={"class": "mobile-login-form-password", "placeholder": "Password"}))
