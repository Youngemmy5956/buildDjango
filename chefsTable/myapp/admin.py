from django.contrib import admin

from .models import Drinks
from .models import MenuCategory
from .models import Menu

# Register your models here.
admin.site.register(Drinks)
admin.site.register(MenuCategory)
admin.site.register(Menu)
