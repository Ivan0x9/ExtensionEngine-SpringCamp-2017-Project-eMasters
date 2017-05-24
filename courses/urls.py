from django.conf.urls import url
from . import views

app_name = 'courses'

urlpatterns = [
    url(r'^$' ,views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #Course urls
    url(r'^courses/add/$', views.CourseCreate.as_view(), name='course-add'),

    url(r'^courses/(?P<pk>[0-9]+)/$', views.CourseUpdate.as_view(), name='course-update'),

    url(r'^courses/(?P<pk>[0-9]+)/delete/$', views.CourseDelete.as_view(), name='course-delete'),

    url(r'^chapter/add/$', views.ChapterCreate.as_view(), name='chapter-add'),

    url(r'^chapter/(?P<pk>[0-9]+)/$', views.ChapterUpdate.as_view(), name='chapter-update'),

    url(r'^chapter/(?P<pk>[0-9]+)/delete/$', views.ChapterDelete.as_view(), name='chapter-delete'),
]
