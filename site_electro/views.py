from django.shortcuts import render

def home(request):
    return render(request, 'Home.html')

def home1(request):
    return render(request, 'home_1.html')

def home2(request):
    return render(request, 'home_2.html')

def home3(request):
    return render(request, 'home_3.html')

def home4(request):
    return render(request, 'home_4.html')