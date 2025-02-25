from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.web_films, name='home'),
    path('login/', LoginView.as_view(template_name='Registration/login.html'), name='login'),
    path('comments/', views.create_comments, name='comments'),
    path('detail/<int:pk>/', views.TitleDetailView.as_view(), name='detail'),
    path('register/', views.register, name='register'),
]