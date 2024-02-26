from django.contrib import admin
from food.models import Item, History, NavbarForm

# Register your models here.
admin.site.register(Item),
admin.site.register(History)
admin.site.register(NavbarForm)