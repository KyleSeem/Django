from __future__ import unicode_literals

from django.db import models
from ..login_reg.models import User

# Create your models here.
class CourseManager(models.Manager):
    def create(self, postData):
        alerts = []
        if len(postData['name']) < 1:
            alerts.append('Course name cannot be left blank.')
            return (False, alerts)
        elif len(postData['description']) < 1:
            alerts.append('Course description cannot be left blank.')
            return (False, alerts)

        else:
            course = Course.objects.create(name=postData['name'])
            Description.objects.create(course_id=course, description=postData['description'])
            alerts.append('Course "{}" successfully added.'.format(course.name))
            return (True, alerts)


    def bridge_connections(self, postData):
        user = User.objects.get(id=int(postData['user']))
        course = Course.objects.get(id=int(postData['course']))
        # print (user.first_name, course.name)
        student = Student.objects.filter(user=user).filter(course=course)
        alerts = []

        if student:
            # print ('Student already registered')
            alerts.append('{} {} is already registered for {}.'.format(user.first_name, user.last_name, course.name))
            return (False, alerts)
        else:
            Student.objects.create(user=user, course=course)
            alerts.append('You have successfully registered {} {} for the {} course.'.format(user.first_name, user.last_name, course.name))
            return (True, alerts)


class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    courseManager = CourseManager()
    objects = models.Manager()

class Description(models.Model):
    description = models.CharField(max_length=255)
    course_id = models.OneToOneField(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField(max_length=500)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
