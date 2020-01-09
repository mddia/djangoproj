from django.contrib import admin

# Register your models here.
from cineseries.models import Cinema, Film, Serie, Realisateur, Acteur, Evenement
from cineseries.models import UserProfileInfo, User

admin.site.register(Cinema)
admin.site.register(Film)
#register serie, realisateur, acteur,
admin.site.register(Serie)
admin.site.register(Realisateur)
admin.site.register(Acteur)
#register template footer
admin.site.register(Evenement)
#fin ajout register lb
admin.site.register(UserProfileInfo) 
