from django.http import JsonResponse
from .models import Post
from django.shortcuts import render, redirect

def decoration_selected_view(request):
    if request.method == 'POST':

        choosion = request.Post.get('decoration')
        title = request.POST.get('title')
        content = request.POST.get('content')
        #post 모델 저장
        title.save()
        content.save()
        choosion.save()
    
        # 출력 확인
        print("제목:", title, "내용:", content, "장식:", decoration)
    
        decoration = request.POST.get('decoration', '0')

    return render(request, 'board/decoration_selected.html')  # GET 요청일 경우 폼을 반환



def index(request):
    return render(request, 'board/index.html')
