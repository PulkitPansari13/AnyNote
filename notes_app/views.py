from django.shortcuts import render,redirect
from django.views.generic import (ListView,DetailView,DeleteView,
                                  CreateView,UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from notes_app.models import Note
from .forms import SignUpForm, LoginForm
# Create your views here.


def index(request):
    return render(request,'notes_app/index.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('notes_app:list_note')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data.get('password1'))
            user.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user1 = authenticate(username=username, password=password)
            login(request,user1)
            return redirect('notes_app:list_note')
    else:
        form = SignUpForm()
    return render(request,'notes_app/signup.html',{'form':form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('notes_app:list_note')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('notes_app:list_note')
    else:
        form = LoginForm()
    return render(request,'notes_app/login.html',{'form':form})


class NoteListView(LoginRequiredMixin,ListView):
    model = Note
    login_url = '/login/'
    # template_name = 'note_list.html'

    def get_queryset(self):
        return self.request.user.notes.all().order_by('-pk')


class NoteDetailView(LoginRequiredMixin,DetailView):
    model = Note
    context_object_name = 'note_details'


class NoteCreateView(LoginRequiredMixin,CreateView):
    model = Note
    # template_name = 'note_form.html'
    fields = ['text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteEditView(LoginRequiredMixin,UpdateView):
    model = Note
    fields = ['text']


class NoteDeleteView(LoginRequiredMixin,DeleteView):
    success_url = reverse_lazy('notes_app:list_note')
    model = Note
    #template_name = 'note_detail.html'
