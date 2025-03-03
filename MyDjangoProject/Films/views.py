from django.shortcuts import render,redirect
from .models import Titles
from .forms import CommentsForm, RegisterForm
from django.views.generic import DetailView
# Create your views here.
def web_films(request):
    films = Titles.objects.all()
    return render(request, 'Films/home.html', {'films': films})

def login(request):
    return render(request, 'Films/login.html')

def create_comments(request):
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CommentsForm()
    return render(request, 'Films/comments.html', {'form': form})

class TitleDetailView(DetailView):
    model = Titles
    template_name = 'Films/detail.html'
    context_object_name = 'films'

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'Registration/register.html', {'form': form})
