from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class EmailManager(models.Manager):
    def validate(self, email):
        if len(email) < 1:
            return (False, 'Email cannot be blank!')
        elif not EMAIL_REGEX.match(email):
            return (False, 'Invalid email address!')
        else:
            return (True, 'Success! The email address "{}" has been registered!'.format(email))

class Email(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # connect manager to Email class
    emailManager = EmailManager()
    # redefine objects so syntax works with ORM
    objects = models.Manager()
