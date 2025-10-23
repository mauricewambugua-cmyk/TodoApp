from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, CreateView, FormView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Todo, Category
from .forms import TodoForm, CategoryForm
from django.urls import reverse_lazy

# Category views
class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'todoapp/add_category.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, 'A category with this name already exists.')
            return redirect('add-category')

class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'todoapp/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)



# todoapp views
class HomeView(LoginRequiredMixin, ListView):
    model = Todo
    form_class = TodoForm
    template_name = 'todoapp/home.html'
    ordering = ['-created_on']
    context_object_name = 'todos'
    success_url = reverse_lazy('home')
    
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user).order_by('-created_on')


#addtodo
class Addview(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todoapp/addtodo.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Only show categories belonging to the current user
        form.fields['category'].queryset = Category.objects.filter(user=self.request.user)
        return form

#deletetodo
class DeleteTodo(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = 'todoapp/deletetodo.html'
    success_url = reverse_lazy('home')


