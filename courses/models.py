from django.db import models
from django.core.urlresolvers import reverse



class Course(models.Model):
    course_name = models.CharField(max_length=25)
    course_logo = models.FileField(null=False, blank=False, default='')
    course_creating_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('courses:detail', kwargs={'pk': self.pk})

    def _str_(self):
        # string repreetnacija objekta
        return self.course_name


class Chapter(models.Model):
    chapter_name = models.CharField(max_length=25)
    chapter_creating_date = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, default=1, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("chapter", kwargs={"course_name": self.course })

    def _str_(self):
        # string repreetnacija objekta
        return   self.chapter_name

class Lesson(models.Model):
    lesson_text = models.CharField(max_length=20)
    chapter_creating_date = models.DateTimeField(auto_now_add=True)
    lesson_fk = models.ForeignKey(Chapter, default=1)