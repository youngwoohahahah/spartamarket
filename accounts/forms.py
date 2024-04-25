from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        # .models imporat users보다 이렇게 하는 게 좋음
        fields = UserCreationForm.Meta.fields
        #+ (필요시 추가필드)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "email",
            "profile_photo"
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.fields.get("password"):
            password_help_text = (
                "You can change the password "'<a href="{}">here</a>.'
            ).format(f"{reverse('accounts:change_password')}")
            self.fields["password"].help_text = password_help_text


class ProfilePhotoChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = [
            "profile_photo"
        ]