from __future__ import unicode_literals

from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
"""
register validation requirements:
    * first/last names: letters only, at least 2 characters;
    * email: not blank, correct format;
    * password: at least 8 characters;
    * confirm_pw: matches password;

login validation requirements:
    * email: matches existing email in database;
    * password: matches corresponding password in database;
"""

class UserManager(models.Manager):
    def register(self, info):
        # pulls and defines POST info from login form
        first_name = str(info['first_name'])
        last_name = str(info['last_name'])
        email = info['email']
        password = info['password']
        confirm_pw = info['confirm_pw']

        alerts = [] # will hold any applicable alerts from validation process

        if len(first_name) < 2:
            alerts.append('First name must be at least 2 characters in length.')
        elif not str.isalpha(first_name):
            alerts.append('First name should contain letters only.')

        if len(last_name) < 2:
            alerts.append('Last name must be at least 2 characters in length.')
        elif not str.isalpha(last_name):
            alerts.append('Last name should contain letters only.')

        if len(email) < 1:
            alerts.append('Email cannot be left blank.')
        elif not EMAIL_REGEX.match(email):
            alerts.append('Invalid email address.')
        try:
            if User.objects.get(email=email):
                alerts.append('The email address "{}" has already been registered.'.format(email))
        except:
            pass

        if len(password) < 8:
            alerts.append('Password must be at least 8 characters in length.')
        elif password != confirm_pw:
            alerts.append('Passwords do not match.')
    # if any validation errors exist, do this:
        if alerts:
            return (False, alerts)
    # in no validation errors exist, do this:
        else:
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            User.objects.create(first_name=first_name, last_name=last_name, email=email, pw_hash=pw_hash)
            alerts.append('Success! Thanks for registering with us!')
            return (True, alerts)

    def login(self, info):
        email = info['email']
        password = info['password']
        alerts = []

        try:
            user = User.objects.get(email=email)
            print ('MATCH')
            print (email, user.email)
            print (user.first_name, user.id)

            if bcrypt.hashpw(password.encode(), user.pw_hash.encode()) != user.pw_hash:
                alerts.append('The password entered is incorrect. Please try again.')
                print ('PASSWORD FAIL')
                print (bcrypt.hashpw(password.encode(), user.pw_hash(encode)))
        except:
            print ('NOT REGISTERED EMAIL')
            alerts.append('The email address "{}" is either incorrect or has not been registered.'.format(email))

        if alerts:
            return (False, alerts)
        else:
            return (True, 'Logged in.', user.first_name)


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    pw_hash = models.CharField(max_length=255) # password post-hash
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # connect UserManager to User model
    userManager = UserManager()
    # redefine objects so other ORM requests work like normal
    objects = models.Manager()
