# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=2048)
    age = models.IntegerField(default=18)
    # True : Female, False: Male
    sex = models.BooleanField(default=False)
    hobby = models.CharField(max_length=4096)

    def __unicode__(self):
        return self.name


class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    math_score = models.IntegerField(default=0)
    english_score = models.IntegerField(default=0)
    physics_score = models.IntegerField(default=0)

    def __unicode__(self):
        return self.student.name + ":" + str(self.math_score)
