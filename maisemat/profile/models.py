from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class MaisematProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    first_name = models.CharField(_(u'First Name'), max_length=30, blank=True, null=True)
    last_name = models.CharField(_(u'Last Name'), max_length=30, blank=True, null=True)
    institution = models.CharField(_(u'Institution'), max_length=100, blank=True, null=True)
    email = models.EmailField(_(u'Email'), max_length=100, blank=True, null=True)
    phone1 = models.CharField(_(u'Phone 1'), max_length=30, blank=True, null=True)
    phone2 = models.CharField(_(u'Phone 2'), max_length=30, blank=True, null=True)
    
