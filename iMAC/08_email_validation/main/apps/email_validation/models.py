from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class EmailManager(models.Manager):
    def validate(self, email):
        if len(email) < 1:
            return (False, 'Email cannot be left blank.')
        elif not EMAIL_REGEX.match(email):
            return (False, 'Not a valid email address.')
        else:
            return (True, 'Success! The email address "{}" has been registered.'.format(email))


class Email(models.Model):
    email = models.EmailField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    emailManager = EmailManager()
    objects = models.Manager()
