from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render , get_object_or_404, redirect
from .models import free_list
from django.utils import timezone


# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def board_free(request):
    Free_list = free_list.objects
    Free_list2 = free_list.objects.all()
    paginator = Paginator(Free_list2,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'board_free.html', {'free_list' :Free_list, 'posts': posts})


def board_detect(request):
    return render(request, 'board_detect.html')

def create_free(request):
    return render(request, 'create_free.html')

def create(request):
    # 새로운 데이터 저장하는 하기 == POST
    Free_list = free_list()
    Free_list.title = request.POST.get('title', '')
    Free_list.body = request.POST.get('body', '')
    Free_list.pub_date = timezone.datetime.now()
    Free_list.save()
    return redirect('http://127.0.0.1:8000/')

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

def detail(request, free_list_id):
    freeDetail = get_object_or_404(free_list, pk=free_list_id)
    return render(request, 'detail_free.html', {'freeDetail':freeDetail, 'free_list_id' : free_list_id})

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
