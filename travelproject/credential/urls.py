from . import views
from django.urls import path
app_name="credential"
urlpatterns=[
    path("registration/",views.registration,name='registration'),
    path("login/",views.login,name="login"),
    path('logout/',views.logout,name='logout')

]