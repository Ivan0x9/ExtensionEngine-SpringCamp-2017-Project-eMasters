from django.db import models
from django.core.urlresolvers import reverse

class Course(models.Model):
    name = models.CharField(max_length=25)
    logo = models.FileField(null=False, blank=False)
    images = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        # string repreetnacija objekta
        return self.name


class Chapter(models.Model):
    name = models.CharField(max_length=25)
    date_created = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def _str_(self):
        # string repreetnacija objekta
        return   self.chapter_name

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    chapter = models.ForeignKey(Chapter)

class TextLesson(Lesson):
    text = models.TextField()

class Multimedia(Lesson):
    link = models.FileField(null=False, blank=False)

class Quiz(Lesson):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

