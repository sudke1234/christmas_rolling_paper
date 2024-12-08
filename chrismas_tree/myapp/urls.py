from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.index, name='index'),  # 기존 index 페이지
    path('decoration_selected/', views.decoration_selected_view, name='decoration_selected'),  # 데이터 선택 페이지
   
]

