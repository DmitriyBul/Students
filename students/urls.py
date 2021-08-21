from django.shortcuts import redirect
from django.urls import path
from . import views

app_name = 'students'
urlpatterns = [
    path('', lambda req: redirect('/home/')),
    path('student/update/<int:pk>/', views.StudentUpdateView.as_view(), name='student_update'),
    path('student/delete/<int:pk>/', views.StudentDeleteView.as_view(), name='student_delete'),
    path('group/add/', views.GroupCreateView.as_view(), name='group_create'),
    path('student/add/', views.StudentCreateView.as_view(), name='student_create'),
    path('home/', views.GroupListView.as_view(), name='group_list'),
    path('group/<slug:slug>/', views.GroupDetailView.as_view(), name='group_detail'),
    path('student/<str:fio>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('group/update/<slug:slug>/', views.GroupUpdateView.as_view(), name='group_update'),
    path('group/delete/<slug:slug>/', views.GroupDeleteView.as_view(), name='group_delete'),
]
