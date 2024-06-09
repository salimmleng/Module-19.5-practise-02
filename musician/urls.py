from django.urls import path 
from .import views

urlpatterns = [
    path('add-musician/', views.MusicianCreateView.as_view(), name='musician'),
    path('edit-musician/<int:id>/', views.MusicianUpdateView.as_view(), name='edit_musician'),
    path('delete/<int:id>/', views.MusicianDeleteView.as_view(), name='delete_musician'),
    path('register/',views.RegisterView.as_view(), name = 'register'),
    path('login/',views.UserLoginView.as_view(), name = 'login'),
    path('logout/',views.UserLogoutView.as_view(), name = 'logout'),
    

]
