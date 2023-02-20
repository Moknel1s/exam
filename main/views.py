from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from django.views import View

from .forms import UserCreationForm


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def reg(request):
    return render(request, 'registration.html')

class Register(View):
    template_name = 'registration/registration.html'


    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password1=password1, password2=password2, email=email, first_name=first_name, last_name=last_name)
            login(request, user)
            return redirect('/')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)