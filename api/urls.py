from django.urls import path
from .views import TaskList,TaskDetail

urlpatterns = [
    path('',TaskList.as_view(),name='list'),
    path('<int:pk>/task',TaskDetail.as_view(),name='list'),
]