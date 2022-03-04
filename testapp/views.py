from multiprocessing import context
from turtle import title
from unicodedata import name
from attr import field, fields
from django.shortcuts import render
from django.http import HttpResponse
from .models import RentIn
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)	

def about(request):
	return render(request,'index.html')

def index(request):
    context = {
        'rentIns':RentIn.objects.all()
    }
    return render(request,"products.html",context)

def home(request):
	return render(request,'home1.html')


def final(request):
	return render(request,'final.html')


class RentInListView(ListView):
	model = RentIn
	template_name = 'products.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'rentIns'

class RentInDetailView(DetailView):
	model = RentIn

class RentInCreateView(LoginRequiredMixin, CreateView):
	model =RentIn
	fields = ['name','image','description','price','stock','created','updated']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class RentInUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = RentIn
	fields = ['name','image','description','price','stock','created','updated']
		
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		rentIn = self.get_object()
		if self.request.user == rentIn.author:
			return True
		return False

class RentInDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = RentIn
	success_url = '/'

	def test_func(self):
		RentIn = self.get_object()
		if self.request.user == RentIn.author:
			return True
		return False

def search(request):
	if 'q' in request.GET:
		q = request.GET['q']
		rentIn = RentIn.objects.filter(name__icontains=q)
	else:
		rentIn = RentIn.objects.all()
	params = {"rentIn" : rentIn }
	return render(request,"search.html",params)

