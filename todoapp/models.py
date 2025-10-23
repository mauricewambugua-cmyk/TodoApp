from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']
        unique_together = ['name', 'user']  # Each user can have unique category names

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('categories')

class Todo(models.Model):
    PRIORITY_CHOICES = [
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low')
    ]

    status_choice = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    status = models.CharField(choices=status_choice, max_length=100, default='PENDING')
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=3,
        help_text='1=High, 2=Medium, 3=Low',
        validators=[
            MinValueValidator(1, message='Priority must be at least 1'),
            MaxValueValidator(3, message='Priority cannot be higher than 3')
        ]
    )
    is_important = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def get_absolute_url(self):
        return reverse("home")

    def __str__(self):
        return self.title + " | " + self.status




 