from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView , LogoutView
from .forms import ChangeUserDataForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from cars.models import Car
from django.contrib.auth.decorators import login_required
from . import forms
from django.views.generic import DetailView ,UpdateView
from .models import History
from cars.models import Car
# Create your views here.

def regestrations(request):
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('regestration')
    else:
        form = forms.UserCreationForm()
    return render(request, 'regestration.html', {'form': form})
    
@method_decorator(login_required , name = 'dispatch')
class UserLogoutView(LogoutView):
    def get_success_url(self) -> str:
        return reverse_lazy('home')

class UserLoginView(LoginView):
    template_name="login.html"
    def get_success_url(self) -> str:
        return reverse_lazy('profile')
    def form_valid(self, form):
        return super().form_valid(form)
    def form_invalid(self, form):
        return super().form_invalid(form)
    
@method_decorator(login_required , name = 'dispatch')
class ProfleView(DetailView):
    template_name='profile.html'
    model = User
    context_object_name = 'user'
    def get_object(self):
        return self.request.user
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history'] = History.objects.filter(user=self.request.user)
        return context
    
class ChangeProfileView(UpdateView):
    model = User
    template_name = 'change_profile.html'
    form_class = ChangeUserDataForm
    success_url = reverse_lazy("profile")
    def get_object(self):
        return self.request.user
    
@method_decorator(login_required , name = 'dispatch')
def ChangeProfileInfo(request):
    if request.method == 'POST':
        form = forms.ChangeUserDataForm(request.POST , instance = request.user)
        if form.is_valid():
            form.save(commit=False)
            return redirect("profile")
    else:
        form = forms.ChangeUserDataForm(instance = request.user)
    return render(request, 'change_profile.html', {'form': form})

    
