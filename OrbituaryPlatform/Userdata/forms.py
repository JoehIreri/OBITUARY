from django import forms
from .models import Userdata

class UserDataForm(forms.ModelForm):
        class Meta:
            model = Userdata
            fields = [
                'first_name',
                'middle_name',
                'last_name',
                'date_of_birth',
                'date_of_death',
                'uology',
                'profile_image'
            ]