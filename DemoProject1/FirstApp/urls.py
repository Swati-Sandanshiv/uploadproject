from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.first_func,name='first_func'),
    path('details/',views.show_details,name='show_details'),
]


# http://127.0.0.1:8000/firstpage/
