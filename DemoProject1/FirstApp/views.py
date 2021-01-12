from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_func(request):
	return HttpResponse('Hello Mumbai, Good Morning...!!!')


def show_details(request):
	return HttpResponse('My details are as: Address: Kharghar, contact: 9876543211')