from django.contrib import admin
from .models import Titles
from .models import Comments

# Register your models here.
admin.site.register(Titles)
admin.site.register(Comments)