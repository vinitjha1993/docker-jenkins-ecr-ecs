from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from myapp.forms import SignUpForm
from  django.contrib.auth.models import User

@login_required
def home(request):
    return render(request, 'myproject/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'myproject/signup.html', {'form': form})
@login_required
def user_info(request):
    query_results=User.objects.all()
    context={'query_results' : query_results}

    return render(request,'myproject/table.html',context)