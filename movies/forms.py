from django import forms
from .models import Reviews
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class ReviewForm(forms.ModelForm):
    """Форма отзыва"""
    captcha = ReCaptchaField()

    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text', 'captcha',)
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control border"}),
            "email": forms.EmailInput(attrs={"class": "form-control border"}),
            "text": forms.Textarea(attrs={"class": "form-control border"})
        }