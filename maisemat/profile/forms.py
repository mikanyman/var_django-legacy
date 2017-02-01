#from django.db import models
from django import forms
from django.forms import ModelForm
from maisemat.profile.models import *
from django.utils.translation import ugettext as _

class ProfileForm(ModelForm):

    first_name = forms.CharField(label=_(u'First Name'), max_length=25, widget=forms.TextInput(attrs={'size':'25'}))
    last_name = forms.CharField(label=_(u'Last Name'), max_length=25, widget=forms.TextInput(attrs={'size':'25'}))
    institution = forms.CharField(label=_(u'Institution'), max_length=50, widget=forms.TextInput(attrs={'size':'50'}))
    email = forms.CharField(label=_(u'Email'), max_length=50, widget=forms.TextInput(attrs={'size':'50'}))
    phone1 = forms.CharField(label=_(u'Phone 1'), max_length=25, required=False, widget=forms.TextInput(attrs={'size':'25'}))
    phone2 = forms.CharField(label=_(u'Phone 2'), max_length=25, required=False, widget=forms.TextInput(attrs={'size':'25'}))

    class Meta:
        model = MaisematProfile
        exclude = ('user')
