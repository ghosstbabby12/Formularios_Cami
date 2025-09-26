from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def admin_login(request):
    # solo renderizamos la plantilla: el form POST apunta al login real del admin
    return render(request, 'admin_login.html')