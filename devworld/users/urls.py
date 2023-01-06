from django.urls import path
from . import views

urlpatterns = [
    path('',views.profiles,name="profiles"),

    path('account/', views.userAccount, name="account"),
    path('edit-profile/', views.editProfile, name="edit-profile"),
    path('profile/<str:pk>',views.viewprofile, name='profile'),
    path('addtech/', views.addTech, name="add-tech"),
    path('deletetech/<str:pk>', views.deleteTech, name="delete-tech"),

    path('login/',views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),

    path('inbox/', views.viewInbox, name="inbox"),
    path('send-message/<str:pk>', views.sendMessage, name="send-message"),
    path('message/<str:pk>/', views.viewMessage, name="message"),
]
