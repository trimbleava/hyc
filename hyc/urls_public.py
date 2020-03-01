from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from ..views import HomeView, ServicesView, AboutView, ContactView, SuccessView


urlpatterns = [
  url(r'^$', HomeView.as_view(), name='root_url_name'),
  url(r'^home$', HomeView.as_view(), name='home_url_name'),
  url(r'^services$', ServicesView.as_view(), name='services_url_name'),
  url(r'^about$', AboutView.as_view(), name='about_url_name'),
  url(r'^contact$', ContactView.as_view(), name='contact_url_name'),
  url(r'^success$', SuccessView.as_view(), name='success_url_name'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns


