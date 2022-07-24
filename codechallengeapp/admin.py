from django.contrib import admin

# Register your models here.

from . models import Place
from . models import bottom

admin.site.register(Place)
admin.site.register(bottom)
