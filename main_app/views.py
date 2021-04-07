from .generateData import generateItemData, generateUserData, generateVoteData
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db.models import Sum, Q
from .models import User, Trip, Vote, Item, Activity, CATEGORIES, ACTIVITIES, getChoices

# Create your views here.


def home(request):
    my_trips = Trip.objects.filter(user_id=request.user.id)
    return render(request, 'index.html', {
        "mytrips": my_trips,
    })


def search(request):
    if request.method == "POST":
        print(request.POST)
        return render(request, "results.html", {
            "destination": request.POST["destination"],
            "activity": request.POST["activity"],
            "date": request.POST["date"]
        })


def searched_filters(request):
    return render(request, 'results.html')


def create(request):
    return redirect('search/new/filters')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


@login_required
def new_trip(request):
    if request.method == "GET":
        activities = getChoices(ACTIVITIES)
        return render(request, "trips/trip_form.html", {
            "title": "Add New Trip",
            "activities": activities

        })
    elif request.method == "POST":
        search = request.POST['search'].split(", ")
        date = request.POST["date"]
        month = date.split("-")[1]
        day = date.split("-")[2]
        if (month == "12" or month == "01" or month == "02" or month == "03"):
            season = "Winter"
        elif(month == "04" or month == "05"):
            season = "Spring"
        elif(month == "06" or month == "07" or month == "08" or month == "09"):
            season = "Summer"
        elif(month == "10" or month == "11"):
            season = "Fall"
        number_items = int(request.POST["number_items"])

        trip = Trip.objects.create(
            user=request.user,
            city=search[0].title(),
            country=search[-1].title(),
            date=date,
            season=season.title(),
            number_items=number_items
        )
        trip.save()

        activities = request.POST.getlist("activities")
        for activity in activities:
            newActivity = Activity.objects.create(
                trip=trip,
                activity=activity,
            )
            newActivity.save()
        return redirect("/trip/%s/" % (trip.id))


@login_required
def trip(request, trip_id):
    if request.method == "GET":
        trip = Trip.objects.get(id=trip_id)
        if trip.user != request.user:
            return redirect("/")

        activities = Activity.objects.filter(trip_id=trip.id)
        filtered_items = []
        for i in range(len(activities)):
            filtered_items_temp = Item.objects.filter(city=trip.city, country=trip.country, season=trip.season, activity=activities[i].activity, trip_id=None, public=True)
            filtered_items.extend(filtered_items_temp)
        filtered_items = list(set(filtered_items))

        filtered_items.extend(Item.objects.filter(trip_id=trip.id))

        items = []
        personal_items = []
        for item in filtered_items:
            sum_votes = Vote.objects.filter(item_id=item.id).aggregate(Sum("vote"))["vote__sum"]
            user_item = Vote.objects.filter(item_id=item.id, user_id=request.user.id)
            if len(user_item) == 1:
                vote = user_item[0]
            else:
                vote = Vote.objects.create(
                    item_id=item.id,
                    user_id=request.user.id,
                    vote=0,
                    checked=False
                )

            if sum_votes == None or sum_votes >= 0:
                if item.trip_id:
                    personal_items.append({
                        "item": item,
                        "sum_votes": sum_votes,
                        "vote": vote,
                        "personal": True
                    })
                else:
                    items.append({
                        "item": item,
                        "sum_votes": sum_votes,
                        "vote": vote,
                        "personal": False
                    })
        sorted_items = sorted(items, key=lambda k: k["sum_votes"], reverse=True)[:trip.number_items]
        sorted_items.extend(personal_items)

        categories = getChoices(CATEGORIES)
        categorized_items = {}
        for category in categories:
            categorized_items[category] = []

        for i in range(len(sorted_items)):
            old_item = sorted_items[i]
            categorized_items[old_item["item"].category].append(old_item)

        return render(request, "trips/trip.html", {
            "title": "%s, %s" % (trip.city, trip.country),
            "categorized_items": categorized_items,
        })


def itemData(request, n=100):
    data = generateItemData(n)
    return render(request, "data.html", {
        "data": data
    })


def userData(request, n=10):
    data = generateUserData(n)
    return render(request, "data.html", {
        "data": data
    })


def voteData(request, n=1000):
    data = generateVoteData(n)
    return render(request, "data.html", {
        "data": data
    })


@ login_required
def upvote_system(request):
    if request.is_ajax and request.method == "POST":
        print("UPVOTE: this is successfully an ajax & post method")
        # this is where the view func will update the database items counters
        # will also create a relation for the user, to check to see if they've previously voted
        return redirect('/')
    else:
        return JsonResponse({"error": ""}, status=400)


@ login_required
def downvote_system(request):
    if request.is_ajax and request.method == "POST":
        print("DOWNVOTE: this is successfully an ajax & post method")
        # this is where the view func will update the database items counters
        # will also create a relation for the user, to check to see if they've previously voted
        return redirect('/')
    else:
        return JsonResponse({"error": ""}, status=400)


@ login_required
def profile(request, user_id):
    my_trips = Trip.objects.filter(user_id=user_id)
    my_items = Item.objects.filter(user=user_id)
    return render(request, 'registration/profile.html', {
        "mytrips": my_trips,
        "myitems": my_items,
    })


def find_city(request):
    return render(request, 'search/search.html')


def results(request):
    print(request.POST)
    search = request.POST['search'].split(", ")
    num_items = 15
    items = Item.objects.filter(city=search[0], country=search[-1])[:num_items]
    print(items)
    categories = getChoices(category)
    sorted_items = {}
    for cat in categories:
        sorted_items[cat] = []
    for item in items:
        if item.vote > 0:
            sorted_items[item.category].append(item)
    return render(request, 'search/results.html', {
        "categories": sorted_items,
    })
