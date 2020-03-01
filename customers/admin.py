from django.contrib import admin

# local
from .models import Client


# Register your models here.

"""
public admin can use admin site to create tenants
so, is good to register this model with admin site.
because this model is a shared model, only authorized
public admin and not authorized tenant can access.
however, a tenant admin can be authorized to access
if invokes the application on public URL.
"""

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('schema_name', 'name')
~                                          
