from django.shortcuts import render,redirect
from .forms import AlbumForm
from .models import Album
# class based

from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView
# Create your views here.

class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)
    

class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'edit_album.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        return super().form_valid(form)





