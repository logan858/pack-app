from django.contrib.auth import views
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path("trip/new/", views.new_trip, name="new_trip"),
    path("trip/<int:trip_id>/", views.trip, name="trip"),
    path("trip/<int:trip_id>/edit", views.edit_trip, name="edit_trip"),
    path("trip/<int:trip_id>/delete", views.delete_trip, name="delete_trip"),
    path("trip/<int:trip_id>/item/add/", views.add_item, name="add_item"),
    path("trip/<int:trip_id>/item/", views.item, name="item"),
    path("trip/<int:trip_id>/item/<int:item_id>/edit/", views.edit_item, name="edit_item"),
    path("trip/<int:trip_id>/item/<int:item_id>/delete/", views.delete_item, name="delete_item"),


    path("trip/upcoming/", views.upcoming_trips, name="upcoming_trips"),
    path("trip/pasts/", views.past_trips, name="past_trips"),


    path("index_search/", views.index_search, name="index_search"),
    path("profile/<int:user_id>/", views.profile, name="profile"),

    path("search/", views.search, name="search"),
    path('search/new/filters', views.searched_filters, name='searched_filters'),
    path('create', views.create, name="create"),

    path("api/vote", views.vote, name="vote"),

    path('findcity/', views.find_city, name="findcity"),
    path('findcity/results', views.results, name='results'),

    # Generate Data
    path("data/item/", views.itemData),
    path("data/item/<int:n>", views.itemData),
    path("data/user/", views.userData),
    path("data/user/<int:n>", views.userData),
    path("data/vote/", views.voteData),
    path("data/vote/<int:n>", views.voteData),
]
