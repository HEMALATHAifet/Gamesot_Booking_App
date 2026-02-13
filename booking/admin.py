

# Register your models here.
from django.contrib import admin
from .models import Game, Booking, Contact

admin.site.register(Game)
admin.site.register(Booking)

admin.site.register(Contact)

