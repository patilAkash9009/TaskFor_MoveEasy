from django.urls import path
from . import views


urlpatterns = [
    path('update/<int:pk>/',views.UpdateUserPosts.as_view()),
    path('posts/',views.ListPost.as_view()),
    path('create/',views.ListUserPosts.as_view()),
    path('delete/<int:pk>/',views.DeleteUserPosts.as_view())
]