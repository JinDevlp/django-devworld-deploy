from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('',views.getRoutes),
    path('posts/',views.getPosts),
    path('posts/<str:pk>',views.getPost),
    path('posts/<str:pk>/rating/',views.postRating),

    path('inbox/',views.getMessages),
    path('inbox/<str:pk>',views.getMessage),

]
