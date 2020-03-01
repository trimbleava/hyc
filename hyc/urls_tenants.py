from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, url
from customers.views import TenantView

urlpatterns = [
    url(r'^$', TenantView.as_view()),
    url(r'^admin/', admin.site.urls),
]
# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns