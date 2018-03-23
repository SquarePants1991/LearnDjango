# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.urls import reverse
from .models import Student

# Create your tests here.

class StudentModelTests(TestCase):

    def test_example(self):
        self.assertIs(1 == 2, False, '1 != 2')

    def test_index_view(self):
        student = Student(name='ocean')
        student.save()
        resposne = self.client.get(reverse('student_detail', args=(1,)))
        print(resposne)
        self.assertIs(resposne.status_code == 200, True)
