from django.db import models
from datetime import *
from django.utils import timezone

# Create your models here.
class Acteur(models.Model):
    nom = models.CharField(max_length=200, null=False, verbose_name='Nom')
    prenom = models.CharField(max_length=200, null=False, verbose_name='Prénom')
    date = models.DateField(default=timezone.now(), blank=True, verbose_name="Date de naissance")
    biographie = models.TextField(null=False, verbose_name='Biographie')
    filmographie = models.TextField(null=False, verbose_name='Filmographie')
    photo = models.FileField(null=False, verbose_name='Photo')
       

    class Meta:
        verbose_name = "Acteur"
        ordering = ['nom']

    def __str__(self):
        return '{}'.format(self.nom)

class Realisateur(models.Model):
    nom = models.CharField(max_length=200, null=False, verbose_name='Nom')
    prenom = models.CharField(max_length=200, null=False, verbose_name='Prénom')
    date = models.DateField(default=timezone.now(), blank=True, verbose_name="Date de naissance")
    biographie = models.TextField(null=False, verbose_name='Biographie')
    filmographie = models.TextField(null=False, verbose_name='Filmographie')
    photo = models.FileField(null=False, verbose_name='Photo')
       

    class Meta:
        verbose_name = "Réalisateur"
        ordering = ['nom']

    def __str__(self):
        return '{}'.format(self.nom) 


class Film(models.Model):
    titre = models.CharField(max_length=200, null=False, verbose_name='Titre')
    resume = models.TextField(null=False, verbose_name='Résumé')
    affiche = models.FileField(null=False, verbose_name='Affiche')
    #ajout model films
    date = models.DateField(default=timezone.now(), blank=True, verbose_name="Date de sortie")
    critiques = models.TextField(null=True, verbose_name='Critiques')
    video = models.CharField(max_length=255, null=True, verbose_name='Vidéo')
    director = models.ForeignKey(Realisateur, on_delete=models.CASCADE)
    players  = models.ManyToManyField(Acteur)

    class Meta:
        verbose_name = "Film"
        ordering = ['titre']

    def __str__(self):
        return '{}'.format(self.titre)

class Cinema(models.Model):
    nom = models.CharField(max_length=30, null=False, verbose_name='Nom du cinéma')
    adresse = models.CharField(max_length=50, null=False, verbose_name='Adresse')
    code_postal = models.CharField(max_length=10, null=False, verbose_name='Code postal')
    ville = models.CharField(max_length=30, null=False, verbose_name='Ville')
    nb_places = models.IntegerField(null=False, verbose_name='Nombre de places')
    #manytomany m'empeche de créér la table cinéma à cause des films à incrémenter
    films = models.ManyToManyField(Film, related_name='cinemas')

    class Meta:
        verbose_name = "Cinéma"
        ordering = ['nom']

    def __str__(self):
        return '{}'.format(self.nom) 

from django.contrib.auth.models import User #Accès aux modèles Django de gestion des utilisateurs
class UserProfileInfo(models.Model): #Infos persos 
    #On lie les infos persos aux infos de connexion gérées par Django à travers la classe User
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='user_profile')
    profile_pic = models.FileField(upload_to='profile_pics',blank=True)
    films = models.ManyToManyField(Film, related_name='users')

    def __str__(self):
        return self.user.username 

#création model série

class Serie(models.Model):
    #le titre n'apparait pas au niveau du volet administrateur
    titre = models.CharField(max_length=200, null=False, verbose_name='Titre épisode')
    date = models.DateField(default=timezone.now(), blank=True, verbose_name="Date de sortie")
    video = models.CharField(max_length=255, null=True, verbose_name='Vidéo')
    saison = models.IntegerField(null=False, verbose_name='Référence Saison')
    resume = models.TextField(null=False, verbose_name='Résumé saison')
    titre = models.CharField(max_length=200, null=False, verbose_name='Titre épisode')
    episode = models.IntegerField(null=False, verbose_name='Référence épisode')
    date = models.DateField(default=timezone.now(), blank=True, verbose_name="Date épisode")
    affiche = models.FileField(null=False, verbose_name='Affiche épisode')
    resume = models.TextField(null=False, verbose_name='Résumé épisode')
    critiques = models.TextField(null=True, verbose_name='Critiques')


    class Meta:
        verbose_name = "Série"
        ordering = ['titre']

    def __str__(self):
        return '{}'.format(self.titre) 


#création model acteur


#création models Evènement
class Evenement(models.Model):
    titre = models.CharField(max_length=200, null=False, verbose_name='Titre')
    resume = models.TextField(null=False, verbose_name='Résumé')
    affiche = models.FileField(null=False, verbose_name='Affiche')
    genre = models.CharField(max_length=200, null=False, verbose_name='Genre')
    auteur = models.CharField(max_length=200, null=True, verbose_name='Auteur')
    compositeur = models.CharField(max_length=200, null=True, verbose_name='Compositeur')
    mise_en_scene = models.CharField(max_length=200, null=False, verbose_name='Mise en scène')
    distibution = models.CharField(max_length=200, null=False, verbose_name='Distribution')
    programmation = models.CharField(max_length=200, null=False, verbose_name='Programmation')
    
    class Meta:
        verbose_name = "Evenement"
        ordering = ['titre']

    def __str__(self):
        return '{}'.format(self.titre)

