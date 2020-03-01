from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from hyc import views

urlpatterns = [
    path(''         , views.testview, name='testview'),                    # http://127.0.0.1:8000/hyc
    path('home/'    ,views.HomeView.as_view(), name='home_url_name'),      # http://127.0.0.1:8000/hyc/home
    path('services/', views.ServicesView.as_view(), name='services_url_name'),
    path('about/'   , views.AboutView.as_view(), name='about_url_name'),
    path('contact/' , views.ContactView.as_view(), name='contact_url_name'),
    path('success/' , views.SuccessView.as_view(), name='success_url_name'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
