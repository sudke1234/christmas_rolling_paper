from django.http import JsonResponse
from .models import Post
from django.shortcuts import render, redirect

# def ecoration_selectded_view(request):
#     if request.method == 'POST':
      
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         #post 모델 저장
#         post = Post.objects.create(title=title, content=content)

#         return redirect('index')
    
#     return render(request, 'board/decoration_selected.html')  # GET 요청일 경우 폼을 반환


def index(request):
    return render(request, 'board/index.html')

def decoration_selected_view(request):
    return render(request, 'board/decoration_selected.html')

def decoration_selectded_view(request):
    if request.method == 'POST':
        new_article = Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            decoration=int(request.POST['decoration'])  # 장식 값 추가
        )
    return redirect('/index/')
    return render(request, 'board/decoration_selected.html')