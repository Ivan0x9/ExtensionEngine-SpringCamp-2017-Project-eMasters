from django.shortcuts import render,reverse
from .forms import CreateUser
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


def home(request):
    context = {
        "title": "EMasters",
        }

    return render(request, "users/home.html", context)


class registration(CreateView):
    form = CreateUser
    model = User
    fields = ['username' ,'password']
    template_name = 'users/register_form.html'
    
    def form_valid(self, form):
        form.instance.save()
        group=Group.objects.get(name='student')
        form.instance.groups.add(group)
        form.save()
        
        return super(registration, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')