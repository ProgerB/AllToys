from django import forms

from .models import User, Toy, Tag


class UserAdminForm(forms.ModelForm):
    email = forms.EmailField(label="User email", required=True)

    class Meta:
        model = User
        fields = "__all__"


class ToyAdminForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        initial = kwargs.pop("initial", None)
        instance = kwargs.pop("instance", None)

        super(ToyAdminForm, self).__init__(*args, **kwargs)

class ToyForm(forms.Form):
    name = forms.CharField(label="Toy name", required=True)
    description = forms.CharField(required=False, widget=forms.Textarea({'cols': '40', 'rows': '3'}))


# class ToyModelForm(forms.ModelForm):
#     class Meta:
#         model = Toy
#         fields = ["name", "description", "type", "photo", "price"]