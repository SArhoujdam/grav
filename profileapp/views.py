import profile
from django.shortcuts import redirect, render
from django.http import HttpResponse
from requests import Response
from django.contrib.auth import authenticate, login as auth_login , logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .modeles import Profileapp

def profile_view(request):
    profile = Profileapp.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})

@login_required

def edit_profile_view(request):
    user = request.user
    profile = Profileapp.objects.get(user=user)

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1', '').strip()
        password2 = request.POST.get('password2', '').strip()
        profile_image = request.FILES.get('profile_image')  # Récupérer l'image de profil

        # Mise à jour du nom et de l'email
        if username:
            user.username = username
        if email:
            user.email = email
        user.save()

        # Mise à jour de la photo de profil
        if profile_image:
            profile.profile_photo = profile_image
            profile.save()

        # Mise à jour du mot de passe
        if password1 and password2:
            if password1 != password2:
                messages.error(request, "Les mots de passe ne correspondent pas.")
                return render(request, 'edit_profile.html', {'profile': profile})

            user.set_password(password1)
            user.save()
            messages.success(request, "Votre mot de passe a été mis à jour.")

        messages.success(request, "Votre profil a été mis à jour.")
        return redirect('profile')

    return render(request, 'edit_profile.html', {'profile': profile})


        
    
def index_view(request):
    return render(request, 'index.html')
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1', '').strip()
        password2 = request.POST.get('password2', '').strip()

        # Vérification que tous les champs sont remplis
        if not all([username, email, password1, password2]):
            messages.error(request, 'Veuillez remplir tous les champs.')
            return render(request, 'register_page.html')

        # Vérification que les mots de passe correspondent
        if password1 != password2:
            messages.error(request, 'Les mots de passe ne correspondent pas.')
            return render(request, 'register_page.html')

        # Vérification si le nom d'utilisateur ou l'email existe déjà
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Ce nom d’utilisateur existe déjà.')
            return render(request, 'register_page.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Cette adresse email est déjà utilisée.')
            return render(request, 'register_page.html')

        # Création de l'utilisateur
        User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request, 'Utilisateur créé avec succès. Vous pouvez maintenant vous connecter.')
        return redirect('login')

    return render(request, 'register_page.html')
def home_view(request):
    profile = Profileapp.objects.get(user=request.user)
    return render(request, 'home.html', {'profile': profile})
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Vérification de l'utilisateur
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redirection vers le tableau de bord
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
            return redirect('login')  # Redirection vers la page de connexion en cas d'erreur
    return render(request, 'login_page.html')
def logout_view(request):
    logout(request)
    return redirect('index') 
