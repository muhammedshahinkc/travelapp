
from . import views
from django.urls import path


urlpatterns=[
    path("",views.demo,name='index'),
    # path("add/",views.addition,name="addition"),

]
