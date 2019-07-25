from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def support(request):
    return render(request, 'support.html')

def pop_tnr(request):
    return render(request, 'pop_tnr.html')

def pop_snack(request):
    return render(request, 'pop_snack.html')

def support_success(request):
    return render(request, 'support_success.html')

def support_success2(request):
    return render(request, 'support_success2.html')