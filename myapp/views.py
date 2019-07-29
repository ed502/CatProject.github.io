from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Cat
from .form import CatPost

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def map(request):
    cats = Cat.objects.order_by('-id')
    cat_list = cats.all()
    paginator = Paginator(cat_list, 3)
    page=request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'map.html', {'cats':cats, 'posts':posts})

def detailMap(request, cat_id):
    cat_detail = get_object_or_404(Cat, pk=cat_id)
    return render(request, 'detailMap.html', {'cat': cat_detail})

def newMap(request):
    # 1. 입력된 내용을 처리하는 기능 -> POST
    # 2. 빈 페이지를 띄워주는 기능 -> GET
    if request.method == 'POST':
        form = CatPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.date = timezone.now()
            post.save()
            return redirect('/detailMap/' + str(post.id))
    else:
        form = CatPost()
        return render(request, 'newMap.html', {'form':form})