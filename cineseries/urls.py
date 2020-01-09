from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),

    path('compte/', views.compte, name='user_account'),
    path('user_register/', views.enregistrement, name='user_register'),
    path('user_login/', views.connexion, name='user_login'),
    path('user_logout/', views.deconnexion, name = 'user_logout'), 

    path('cinemas/list', views.cinemas, name='cinemas'),
    path('cinemas/cinema/<int:id_cinema>', views.cinema, name='cinema'),

    path('films/list', views.films, name='films'),
    path('films/film/<int:id_film>', views.film, name='film'),

    path('films/film/favorite/<int:id_film>', views.favorite, name='favorite'),
    path('films/film/unfavorite/<int:id_film>', views.unfavorite, name='unfavorite'), 

    #ajout views suite à création des modèles séries, réalisateurs et acteurs
    path('series/list', views.series, name='series'),
    path('series/serie/<int:id_serie>', views.serie, name='serie'),

    path('realisateurs/list', views.realisateurs, name='realisateurs'),
    path('realisateurs/realisateur/<int:id_realisateur>', views.realisateur, name='realisateur'),

    path('acteurs/list', views.acteurs, name='acteurs'),
    path('acteurs/acteur/<int:id_acteur>', views.acteur, name='acteur'),
    #fin ajout urls lb
    #ajout url footer
    path('evenements/list', views.evenements, name='evenements'),
    path('evenements/evenement/<int:id_evenement>', views.evenement, name='evenement'),

    path('e_mails/list', views.e_mails, name='e_mails'),
    path('e_mails/e_mail/<int:id_e_mail>', views.e_mail, name='e_mail'),

    path('abonnements/list', views.abonnements, name='abonnements'),
    path('abonnements/abonnement/<int:id_abonnement>', views.abonnement, name='abonnement'),

    path('ateliers/list', views.ateliers, name='ateliers'),
    path('ateliers/atelier/<int:id_atelier>', views.atelier, name='atelier'),

    path('avis/list', views.avis, name='avis'),
    path('avis/avis/<int:id_avis>', views.avis, name='avis'),

    path('recrutements/list', views.recrutements, name='recrutements'),
    path('recrutements/recrutement/<int:id_recrutement>', views.recrutement, name='recrutement'),

    path('politiques_de_confidentialite/list', views.politiques_de_confidentialite, name='politiques_de_confidentialite'),
    path('politiques_de_confidentialite/politique_de_confidentialite/<int:id_politique_de_confidentialite>', views.politique_de_confidentialite, name='politique_de_confidentialite'),

    path('mentions_legales/list', views.mentions_legales, name='mentions_legales'),
    path('mentions_legales/mention_legale/<int:id_mention_legale>', views.mention_legale, name='mention_legale'),
    #fin ajout url footer
] 
