from django.urls import path,include
from .import views
urlpatterns = [
   path('',views.AlbumCreateView.as_view(),name = 'add_album'),
   path('edit/<int:id>',views.AlbumUpdateView.as_view(), name = 'edit_album'),
   

]
