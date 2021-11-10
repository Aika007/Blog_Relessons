from django.urls import path
from .views import contact, hello_world, about, post

app_name = 'blog'

urlpatterns = [
    path("hello/", hello_world, name='index'),
    path("about/", about, name='about'),
    path("contact/", contact, name='contact'),
    path("post/", post, name='post') ,
]