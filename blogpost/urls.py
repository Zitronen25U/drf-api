
from django.contrib import admin
from django.urls import path 

from .views import blogpostlist, blogpostdetail



urlpatterns = [
    path('',blogpostlist.as_view(), name='blogpostlist'),
    path('<int:pk>/', blogpostdetail.as_view(), name="blogpostdetail")

]