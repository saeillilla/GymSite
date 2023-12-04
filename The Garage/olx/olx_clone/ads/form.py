from django import forms
from ads.models import *
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import UserCreationForm


from django import forms
from .models import *

from django import forms
from .models import Ad, Category, Disctrict

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['ad_title', 'description', 'price', 'photo1', 'photo2', 'photo3', 'photo4', 'address', 'category', 'district']

    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AdForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['user'].initial = user
            self.fields['user'].widget = forms.HiddenInput()
            self.fields['user'].disabled = True

        # Dynamically set the queryset for the category and district fields
        self.fields['category'].queryset = Category.objects.all()
        self.fields['district'].queryset = Disctrict.objects.all()

    def save(self, commit=True):
        ad = super(AdForm, self).save(commit=False)
        if hasattr(self, 'user') and self.user:
            ad.user = self.user
        if commit:
            ad.save()
        return ad
    

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_name', 'vehicle_model', 'vehicle_color',
                  'vehicle_mileage', 'price', 'vehicle_number', 'vehicle_insurance',
                  'accident_record', 'vehicle_fine_record', 'photo1', 'photo2',
                  'photo3', 'photo4']
        user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())
        def __init__(self, *args, **kwargs):
            user = kwargs.pop('user', None)
            super(AdForm, self).__init__(*args, **kwargs)

            if user:
                self.fields['user'].initial = user
                self.fields['user'].widget = forms.HiddenInput()
                self.fields['user'].disabled = True
        def save(self, commit=True):
            ad = super(VehicleForm, self).save(commit=False)
            if hasattr(self, 'user') and self.user:
                ad.user = self.user
            if commit:
                ad.save()
            return ad
        


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


from django.contrib.auth.forms import AuthenticationForm

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True}),
    )


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street','landMark', 'city', 'state', 'postal_code', 'country']

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        # Add any additional customization for form fields if needed