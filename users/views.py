from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login


class registerview(generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Save the new user
        response = super().form_valid(form)
        user = form.save()
        # Log the user in
        login(self.request, user)
        messages.success(self.request, 'Registration successful. You are now logged in.')
        return response
    


