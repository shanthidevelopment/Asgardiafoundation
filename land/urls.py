# your_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page route
    
    path('about/', views.about, name='about'),  # About page route
    
    path('get_involved/', views.get_involved, name='get_involved'),  # Get Involved page route
    
    path('event/', views.event, name='event'),  # Event page route
    
    path('gallery/', views.gallery, name='gallery'),  # Gallery page route
    
    path('employement/', views.employement, name='employement'),  # Employment page route
    
    path('womenempowerment/', views.women_empowerment, name='women_empowerment'),  # Women Empowerment page route
    
    path('education/', views.education, name='education'),  # Education page route
    
    path('health/', views.health, name='health'),  # Health page route
    
    path('environment/', views.environment, name='environment'),  # Environment page route
    
    path('daily/', views.daily_meals, name='daily_meals'),  # Daily Meals page route
    
    path('live/', views.livelihood, name='livelihood'),  # Livelihood page route
    
    path('csr/', views.csr_impact, name='csr_impact'),  # CSR Impact page route
    
    path('contact/', views.contact, name='contact'),  # Contact page route
]
