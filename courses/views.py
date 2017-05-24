from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views import  generic
from django.views.generic import  View
from django.views import generic
from .models import Course, Chapter, Lesson


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'courses/index.html'
    context_object_name = 'all_courses'

    def get_queryset(self):
        return Course.objects.all()

class DetailView(generic.DetailView):
    model = Course
    template_name = 'courses/detail.html'

#Course
class CourseCreate(CreateView):
    model = Course
    fields = ['name', 'logo', 'images']

class CourseUpdate(UpdateView):
    model = Course
    fields = ['name', 'logo', 'images']

class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:index')

#Chapter
class ChapterCreate(CreateView):
    model = Chapter
    fields = ['name', 'date_created']

    def form_valid(self,form):
        form.instance.course=self.kwargs['pk']
        return super(ChapterCreate, self).form_valid(form)

class ChapterUpdate(UpdateView):
    model = Chapter
    fields = ['name', 'date_created']

class ChapterDelete(DeleteView):
    model = Chapter
    success_url = reverse_lazy('courses:detail')

#Lesson

class LessonCreate(CreateView):
    model = Lesson
    fields = ['title', 'date_created', 'chapter']

class LessonUpdate(UpdateView):
    model = Lesson
    fields = ['title', 'date_created', 'chapter']

class LessonDelete(UpdateView):
    model = Lesson
    success_url = reverse_lazy('courses:detail')




