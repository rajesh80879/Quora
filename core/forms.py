from django import forms
from .models import Question, Answer
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import CustomUser
import re


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["name", "email", "password1", "password2"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter your full name"}),
            "email": forms.EmailInput(attrs={"placeholder": "example@gmail.com"}),
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        validate_email(email)
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Email is already registered.")

        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2:
            raise ValidationError("Passwords do not match.")

        if len(password1) < 8:
            raise ValidationError("Password must be at least 8 characters long.")

        if not re.search(r"[A-Z]", password1):
            raise ValidationError(
                "Password must contain at least one uppercase letter."
            )

        if not re.search(r"[a-z]", password1):
            raise ValidationError(
                "Password must contain at least one lowercase letter."
            )

        if not re.search(r"\d", password1):
            raise ValidationError("Password must contain at least one digit.")

        if not re.search(r"[^\w\s]", password1):
            raise ValidationError(
                "Password must contain at least one special character."
            )

        return password2


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["title", "description"]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["content"]
