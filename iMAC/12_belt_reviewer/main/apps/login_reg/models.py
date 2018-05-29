from __future__ import unicode_literals

from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class UserManager(models.Manager):
    def login(self, postData):
        email = postData['email']
        password = postData['password']

        alerts = []

        try:
            user = User.objects.get(email=email)
        except:
            print ('EMAIL NOT REGISTERED')
            alerts.append('The email address "{}" is either incorrect or has not been registered.'.format(email))
            return (False, alerts)
        else:
            if email == user.email:
                if bcrypt.hashpw(password.encode(), user.pw_hashed.encode()) == user.pw_hashed:
                    # print ('it matches', user.id)
                    return (True, 'back, {}! You have successfully logged in.'.format(user.first_name), user.id)
                else:
                    # print ('no pw match')
                    alerts.append('The password entered is incorrect. Please try again.')

            if alerts:
                return (False, alerts)


    def register(self, postData):
        # grabs user input from registration form
        first_name = str(postData['first_name'])
        last_name = str(postData['last_name'])
        email = postData['email']
        password = postData['password']
        pw_verify = postData['pw_verify']

        alerts = []

        if len(first_name) < 2:
            alerts.append('First name must be at least 2 characters in length.')
        elif not str.isalpha(first_name):
            alerts.append('First name must contain letters only.')

        if len(last_name) < 2:
            alerts.append('Last name must be at least 2 characters in length.')
        elif not str.isalpha(last_name):
            alerts.append('Last name must contain letters only.')

        if len(email) < 1:
            alerts.append('Email cannot be left blank.')
        elif not EMAIL_REGEX.match(email):
            alerts.append('Invalid email address.')

        if len(password) < 8:
            alerts.append('Password must be at least 8 characters in length.')
        elif password != pw_verify:
            alerts.append('Passwords do not match.')

        if alerts:
            return (False, alerts)

        else:
            pw_hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = User.objects.create(first_name=first_name, last_name=last_name, email=email, pw_hashed=pw_hashed)
            return (True, 'aboard, {}! You have successfully registered.'.format(first_name), user.id)


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    pw_hashed = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    userManager = UserManager()
    objects = models.Manager()
