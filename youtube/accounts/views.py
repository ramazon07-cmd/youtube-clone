from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


# Create your views here.


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return redirect('/')
    