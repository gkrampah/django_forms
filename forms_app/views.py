from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    context ={}
    context['form']= "Hello world"
    return render(request, 'forms_app/index.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('forms_app-login')
    else:
        form = UserRegisterForm()
    return render(request, 'forms_app/register.html', {'form': form})

#forces the user to login to access this url
@login_required
def profile(request):
    
    return render(request, 'forms_app/profile.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('forms_app-profile')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }

    return render(request, 'forms_app/profile.html', context)