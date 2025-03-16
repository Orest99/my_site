from django.shortcuts import render

def home(request):
    context = {'title':'Home Page'}
    return render(request, 'Home.html', context)

def home1(request):
    context = {'title':'Page1'}
    return render(request, 'home_1.html', context)

def home2(request):
    context = {'title':'Page2'}
    return render(request, 'home_2.html', context)

def home3(request):
    context = {'title':'Page3'}
    return render(request, 'home_3.html', context)

def home4(request):
    context = {'title':'Page4'}
    return render(request, 'home_4.html', context)