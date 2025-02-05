# your_app/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'asgardia/index.html')  # Home page

def about(request):
    return render(request, 'asgardia/about.html')  # About page

def get_involved(request):
    return render(request, 'asgardia/Get_Involved.html')  # Get Involved page

def event(request):
    return render(request, 'asgardia/event.html')  # Event page

def gallery(request):
    return render(request, 'asgardia/gallery.html')  # Gallery page

def employement(request):
    return render(request, 'asgardia/employement.html')  # Employment page

def women_empowerment(request):
    return render(request, 'asgardia/womenempowerment.html')  # Women Empowerment page

def education(request):
    return render(request, 'asgardia/education.html')  # Education page

def health(request):
    return render(request, 'asgardia/health.html')  # Health page

def environment(request):
    return render(request, 'asgardia/environment.html')  # Environment page

def daily_meals(request):
    return render(request, 'asgardia/daily.html')  # Daily Meals page

def livelihood(request):
    return render(request, 'asgardia/live.html')  # Livelihood page

def csr_impact(request):
    return render(request, 'asgardia/csr.html')  # CSR Impact page

def contact(request):
    return render(request, 'asgardia/contact.html')  # Contact page
