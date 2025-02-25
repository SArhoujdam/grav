# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .modeles import Profileapp

# Créer le profil de l'utilisateur lorsque le compte utilisateur est créé
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profileapp.objects.create(user=instance)

# Sauvegarder le profil de l'utilisateur lorsque les informations de l'utilisateur sont mises à jour
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Sauvegarder l'objet Profileapp associé à l'utilisateur
    instance.profileapp.save()

