# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Student, Score

def index(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, "admin/index.html", context)


def student_detail(request, student_id):
    student = Student.objects.get(pk=student_id)
    context = {
        'student_managment': student
    }
    return render(request, "admin/detail.html", context)

def score_detail(request, student_id):
    score = Score.objects.get(student_id=student_id)
    context = {
        'score': score
    }
    return render(request, "admin/score.html", context)