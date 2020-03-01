from django.db import models

# third party
from tenant_schemas.models import TenantMixin

# local


# Create your models here.


class Client(TenantMixin):
    # from super (domain_url, schema_name)
    client_id = models.AutoField(verbose_name='Client ID', primary_key=True)
    name = models.CharField(verbose_name='Client Name', max_length=254, null=True, blank=True)
    email = models.EmailField(verbose_name='Email', max_length=254, null=True, blank=True)
    phone = models.CharField(verbose_name='Phone Number', max_length=254, null=True, blank=True)
    description = models.TextField(verbose_name='Description',max_length=200)
    created_on = models.DateField(auto_now_add=True)
    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

    def __str__(self):
        return self.name

