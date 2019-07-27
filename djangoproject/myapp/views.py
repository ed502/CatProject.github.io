from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def board_free(request):
    return render(request, 'board_free.html')

def board_detect(request):
    return render(request, 'board_detect.html')
    