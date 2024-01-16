# manager/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Password, Profile
from .forms import NoteForm, PasswordForm,SignUpForm
# from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

def home(request):
    return render(request, 'manager/home.html')




@login_required(login_url='user_login')  
def notes_list(request):
    try:
        profile = request.user.profile
        notes = Note.objects.filter(profile=profile)
        return render(request, 'manager/notes_list.html', {'notes': notes})
    except Profile.DoesNotExist:
        # Handle the case where the profile does not exist for the user
        # You can redirect to a page where the user can create their profile, for example.
        return render(request, 'manager/profile_not_found.html')

@login_required(login_url='user_login')  
def passwords_list(request):
    try:
        profile = request.user.profile
        passwords = Password.objects.filter(profile=profile)
        return render(request, 'manager/passwords_list.html', {'passwords': passwords})
    except Profile.DoesNotExist:
        # Handle the case where the profile does not exist for the user
        # You can redirect to a page where the user can create their profile, for example.
        return render(request, 'manager/profile_not_found.html')
    

@login_required(login_url='user_login')  
def add_note(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            Note.objects.create(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                profile=profile
            )
            return redirect('user_home')
    else:
        form = NoteForm()

    return render(request, 'manager/add_note.html', {'form': form})


# def add_note(request):
#     if request.method == 'POST':
#         form = NoteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('notes_list')
#     else:
#         form = NoteForm()
#     return render(request, 'manager/add_note.html', {'form': form})

@login_required(login_url='user_login')  
def add_password(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            Password.objects.create(
                website=form.cleaned_data['website'],
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                profile=profile
            )
            return redirect('user_home')
    else:
        form = PasswordForm()

    return render(request, 'manager/add_password.html', {'form': form})


# def add_password(request):
#     if request.method == 'POST':
#         form = PasswordForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('passwords_list')
#     else:
#         form = PasswordForm()
#     return render(request, 'manager/add_password.html', {'form': form})




def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.delete()
    return redirect('notes_list')
    
    

def delete_password(request, password_id):
    password = get_object_or_404(Password, pk=password_id)
    password.delete()
    return redirect('passwords_list')
    
    
    
# def login_view(request):
#     if request.method=='POST':
#         print(request.POST)
#         mail=request.POST.get('email')
#         password=request.POST.get('password')
#         user=User.objects.create(username=mail,password=password)
#         user.save()
#         return redirect('/')
#     return render(request,'manager/login.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():     
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)  # Log in the user after registration
            return redirect('user_home')  # Redirect to the user's home page
    else:
        form = SignUpForm()

    return render(request, 'manager/sign_up.html', {'form': form})

# def login(request):
#     user=user.objects.get(username=user)
#     notes=Note.objects.filter(user=user)
#     passw=Password.objects.filter(user=user)
    

def userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirect to the user's home page (you can replace 'user_home' with the desired URL)
                return redirect('user_home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'manager/login.html', {'form': form})


@login_required(login_url='user_login')
def user_home(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        return render(request, 'manager/profile_not_found.html')

    notes = Note.objects.filter(profile=profile)
    passwords = Password.objects.filter(profile=profile)

    return render(request, 'manager/user_home.html', {'notes': notes, 'passwords': passwords})
    
    
def profile_not_found(request):
    return render(request,'profile_not_found.html')