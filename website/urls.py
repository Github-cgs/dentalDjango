
from django.urls import path
from . import views

urlpatterns = [
	path ('', views.home, name="home"),  
	path('contact.html', views.contact, name='contact'),
	path('galeria.html', views.galeria, name='galeria'),
	path('pricing.html', views.pricing, name='pricing'),
	path('service.html', views.service, name='service'),
]