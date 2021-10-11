from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request , 'hybrid/dashboard.html')

def profile(request):
	return render(request , 'hybrid/profile.html')

def manage(request):
	return render(request , 'hybrid/manage.html')

def logout(request):
	return render(request , 'hybrid/logout.html')

