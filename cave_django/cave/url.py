from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='UserList'),
    path('users/<int:pk>', views.UserList, name='UserDetail'),
    path('comments/', views.CommentList.as_view(), name='CommentList'),
    path('comments/<int:pk>', views.CommentList, name='CommentDetail'),
]