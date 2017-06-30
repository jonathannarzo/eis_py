from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserForm, ProfileForm, RoleForm
from .role import role_required
from .models import Profile

@login_required
def profile(request):
    context = {}
    return render(request, 'users/profile.html', context)

@role_required(2)
def create_user(request):
    user_form = UserForm(request.POST or None)
    user_profile_form = ProfileForm(request.POST or None)

    if request.method == 'POST':
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.is_superuser = False
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            userprofile = user_profile_form.save(commit=False)
            userprofile.user = user
            userprofile.save()
            messages.success(request, 'User Successfully Created.')
            return redirect('users:create');

    context = {
        'user_form': user_form,
        'user_profile_form': user_profile_form,
    }

    return render(request, 'users/create_user.html', context)

@role_required(2)
def create_role(request):
    role_form = RoleForm(request.POST or None)

    if request.method == 'POST':
        if role_form.is_valid():
            role_form.save()
            messages.success(request, 'Role Successfully Created.')
            return redirect('users:roles');

    context = {
        'role_form':role_form
    }
    
    return render(request, 'users/create_role.html', context)

@role_required(2)
def list_users(request):
    queryset_list = Profile.objects.all()
    context = {
        'employees': queryset_list
    }
    return render(request, 'users/list_users.html', context)
