from django.shortcuts import render,redirect
from .forms import MusicianForm
from .models import Musician
#class based
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.edit import CreateView,UpdateView,FormView,DeleteView
from .forms import RegistrationForm

# Create your views here.


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)




class UserLoginView(LoginView):
    template_name = 'login.html'
    

    def form_valid(self,form):
        return super().form_valid(form)

    def form_invalid(self,form):
        return super().form_invalid(form)
    
  
    def get_success_url(self):
        return reverse_lazy('login')


class UserLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('login')



class MusicianCreateView(LoginRequiredMixin, CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'music.html'
    success_url = reverse_lazy('home')

    login_url = '/login/'
    redirect_field_name = 'index'

    def form_valid(self, form):
        return super().form_valid(form)






class MusicianUpdateView(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'edit.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        return super().form_valid(form)



class MusicianDeleteView(DeleteView):
    model = Musician
    template_name = 'delete.html'  
    success_url = reverse_lazy('home')  
    pk_url_kwarg = 'id' 