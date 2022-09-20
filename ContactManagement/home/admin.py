from django.contrib import admin

# Register your models here.
from .models import Register

class NewUser(admin.ModelAdmin):
    pass
admin.site.register(Register)