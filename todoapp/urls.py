from django.urls import path
from .views import HomeView, Addview, DeleteTodo, CategoryCreateView, CategoryListView

# todoapp urls
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('addtodo/', Addview.as_view(), name='addtodo'),
    path('delete/<int:pk>/', DeleteTodo.as_view(), name='delete'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/add/', CategoryCreateView.as_view(), name='add-category'),
]