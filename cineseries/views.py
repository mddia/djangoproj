from django.shortcuts import render

# Create your views here.
from django.urls import resolve #permet d'accéder aux fonctions liées aux urls
#import des views suite à la création des models séries, réalisateurs et acteurs
from .models import Cinema, Film, Serie, Realisateur, Acteur,Evenement #permet d'accéder aux classes du modèle de données

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from cineseries.forms import UserForm,UserProfileInfoForm 

#import des views suite à la création des models Série, Réalisateur et Acteur


def home(request):
    return render(request, 'index.html', {})

def cinemas(request):
    tousLesCinemas = Cinema.objects.all()
    print(tousLesCinemas)
    return render(request, 'cinemas.html', {'cinemas': tousLesCinemas})

def cinema(request, id_cinema):
    varCinema = Cinema.objects.get(id=id_cinema)
    return render(request, 'cinema.html', {'cinema': varCinema})

def films(request):
    tousLesFilms = Film.objects.all()
    print('test {}'.format(tousLesFilms))
    return render(request, 'films.html', {'films': tousLesFilms})

def film(request, id_film):
    varFilm = Film.objects.get(id=id_film)
    return render(request, 'film.html', {'film': varFilm}) 

#ajout def suite à création des models Série, Réalisateur et Acteur
def series(request):
    tousLesSeries = Serie.objects.all()
    return render(request, 'series.html', {'series': tousLesSeries})

def serie(request, id_serie):
    varSerie = Serie.objects.get(id=id_serie)
    return render(request, 'serie.html', {'serie': varSerie}) 


def realisateurs(request):
    tousLesrealisateurs = Realisateur.objects.all()
    return render(request, 'realisateurs.html', {'realisateurs': tousLesrealisateurs})

def realisateur(request, id_realisateur):
    varRealisateur = Realisateur.objects.get(id=id_realisateur)
    return render(request, 'realisateur.html', {'realisateur': varRealisateur})

def acteurs(request):
    tousLesActeurs = Acteur.objects.all()
    print('test {}'.format(tousLesActeurs))
    return render(request, 'acteurs.html', {'acteurs': tousLesActeurs})

def acteur(request, id_acteur):
    varActeur = Acteur.objects.get(id=id_acteur)
    return render(request, 'acteur.html', {'acteur': varActeur}) 

#fin ajout views

#ajout vews footer
def evenements(request):
    tousLesEvenements = Evenement.objects.all()
    print('test {}'.format(tousLesEvenements))
    return render(request, 'evenements.html', {'evenements': tousLesEvenements})

def evenement(request, id_evenement):
    varEvenement = Evenement.objects.get(id=id_evenement)
    return render(request, 'evenement.html', {'evenement': varEvenement}) 

def e_mails(request):
    tousLesE_mails = E_mail.objects.all()
    print('test {}'.format(tousLesE_mails))
    return render(request, 'e_mails.html', {'e_mails': tousLesE_mails})

def e_mail(request, id_e_mail):
    varE_mail = E_mail.objects.get(id=id_e_mail)
    return render(request, 'e_mail.html', {'e_mail': varE_mail}) 

def abonnements(request):
    tousLesAbonnements = Abonnement.objects.all()
    print('test {}'.format(tousLesAbonnements))
    return render(request, 'abonnements.html', {'abonnements': tousLesAbonnements})

def abonnement(request, id_abonnement):
    varAbonnement = Abonnement.objects.get(id=id_abonnement)
    return render(request, 'abonnement.html', {'abonnement': varAbonnement}) 

def ateliers(request):
    tousLesAteliers = Atelier.objects.all()
    print('test {}'.format(tousLesAteliers))
    return render(request, 'ateliers.html', {'ateliers': tousLesAteliers})

def atelier(request, id_atelier):
    varAtelier = Atelier.objects.get(id=id_atelier)
    return render(request, 'atelier.html', {'atelier': varAtelier})

def avis(request):
    tousLesAvis = Avis.objects.all()
    print('test {}'.format(tousLesAvis))
    return render(request, 'avis.html', {'avis': tousLesAvis})

def avis(request, id_avis):
    varAvis = Avis.objects.get(id=id_avis)
    return render(request, 'avis.html', {'avis': varAvis}) 

def recrutements(request):
    tousLesRecrutements = Recrutement.objects.all()
    print('test {}'.format(tousLesRecrutements))
    return render(request, 'recrutements.html', {'recrutements': tousLesRecrutements})

def recrutement(request, id_recrutement):
    varRecrutement = Recrutement.objects.get(id=id_recrutement)
    return render(request, 'recrutement.html', {'recrutement': varRecrutement})

def politiques_de_confidentialite(request):
    tousLesPolitiques_de_confidentialite = Politique_de_confidentialite.objects.all()
    print('test {}'.format(tousLesPolitiques_de_confidentialite))
    return render(request, 'politiques_de_confidentialite.html', {'politiques_de_confidentialite': tousLesPolitiques_de_confidentialite})

def politique_de_confidentialite(request, id_politique_de_confidentialite):
    varPolitique_de_confidentialite = Politique_de_confidentialite.objects.get(id=id_politique_de_confidentialite)
    return render(request, 'politique_de_confidentialite.html', {'politique_de_confidentialite': varPolitique_de_confidentialite}) 

def mentions_legales(request):
    tousLesMentions_legales = Mention_legale.objects.all()
    print('test {}'.format(tousLesMentions_legales))
    return render(request, 'mentions_legales.html', {'mentions_legales': tousLesMentions_legales})

def mention_legale(request, id_mention_legale):
    varMention_legale = Mention_legale.objects.get(id=id_mention_legale)
    return render(request, 'mention_legale.html', {'mention_legale': varMention_legale}) 
#fin ajout views footer

def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Compte inactif.")
        else:
            print("Tentative de login échoué.")
            print("Informations utilisées: login {} / password: {}".format(username,password))
            return HttpResponse("Informations d'authentification invalides")
    else:
        return render(request, 'login.html', {}) 

def enregistrement(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                #print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'enregistrement.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered
                           }) 

@login_required
def deconnexion(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def compte(request):
    return render(request, 'compte.html', {}) 

@login_required
def favorite(request, id_film):
    film = Film.objects.get(id=id_film)
    user = request.user

    if (hasattr(user, 'user_profile')):
        userProfile = user.user_profile
        userProfile.films_preferes.add(film)

    return HttpResponseRedirect(reverse('film', args=[id_film])) 

@login_required
def unfavorite(request, id_film):
    film = Film.objects.get(id=id_film)
    user = request.user

    if (hasattr(user, 'user_profile')):
        userProfile = user.user_profile
        userProfile.films_preferes.remove(film)


