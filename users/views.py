from django.shortcuts import render,reverse,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic.base import RedirectView
from django.views.generic import FormView
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
def home(request):
    context = {
        "title": "EMasters",
        }

    return render(request, "users/home.html", context)


class registration(CreateView):
    form = UserCreationForm
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


class LoginView(FormView):
    form_class = AuthenticationForm
    success_url = 'users/home.html'
    template_name = 'users/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(self.request, user)

        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')

class LogoutView(RedirectView):

    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)