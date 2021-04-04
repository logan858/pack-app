from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("search/", views.search, name="search"),
    # path('search/', views.search_city, name='search_city'),
    path('search/new', views.searched_city, name='searched_city'),
    path('search/new/filters', views.searched_filters, name='searched_filters'),
    path('create', views.create, name="create"),
    path('accounts/signup', views.signup, name='signup'),

    path("test", views.test, name="test")
]
