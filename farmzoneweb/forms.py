from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    """

    @param commit:
    @return:
    """
    email = forms.EmailField(required=True)

    class Meta:
        """

        @param commit:
        @return:
        """
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        """

        @param commit:
        @return:
        """
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
