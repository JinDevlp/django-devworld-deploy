from django.urls import path
from . import views

urlpatterns = [
# path('',views.homepage, name='home'),
path('',views.posts, name='posts'),
path('post/<str:pk>',views.viewPost, name='single-post'),
path('edit-post/<str:pk>',views.editPost, name='edit-post'),
path('delete-post/<str:pk>',views.deletePost, name='delete-post'),
path('addpost/',views.addPost, name='add-post'),
]
