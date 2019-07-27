from django.shortcuts import render
from .models import free_list


# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def board_free(request):
    return render(request, 'board_free.html')

def board_detect(request):
    return render(request, 'board_detect.html')

def create_free(request):
    return render(request, 'create_free.html')

def create(request):
    # 새로운 데이터 저장하는 하기 == POST
    



    

def read(request):

   # policyCount = PolicyList.objects.count()
    freeCount = free_list.objects.count()
    #policies = PolicyList.objects.all()
    frees = free_list.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(frees,10)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    #return render(request,'policyList.html' , {'policies':policies, 'posts':posts, 'policyCount':policyCount})
    return render(request,'board_free.html' , {'frees':frees, 'posts':posts, 'freeCount':freeCount})


