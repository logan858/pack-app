from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from datetime import datetime

SEASONS = (
    ('AL', 'All'),
    ('WT', 'Winter'),
    ('SP', 'Spring'),
    ('SM', 'Summer'),
    ('FL', 'Fall'),
)

ACTIVITIES = (
    ("AL", "All"),
    ("BP", "Backpacking"),
    ("BS", "Business"),
    ("LS", "Leisure"),
    ("SS", "Sightseeing"),
    ("OT", "Other")
)

AGES = (
    ("A", "All Ages"),
    ("I", "Infant"),
    ("C", "Child"),
    ("T", "Teen"),
    ("A", "Adult"),
    ("S", "Senior")
)

GENDERS = (
    ("A", "All"),
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other")
)

CATEGORIES = (
    ("CL", "Clothing"),
    ("EL", "Electronics"),
    ("EQ", "Equipment"),
    ("PS", "Personal"),
    ("MD", "Medication"),
    ("OT", "Other"),
)

NUMBERS_ITEMS = [{
        "name" : "Light",
        "text_1" : "Less than 10 items",
        "num" : 10,
        "id" : "number_items_light"
    },{
        "name" : "Medium",
        "text_1" : "10 - 15",
        "text_2" : "items",
        "num" : 15,
        "id" : "number_items_medium"
    }, {
        "name" : "Heavy",
        "text_1" : "15 - 20",
        "text_2" : "items",
        "num" : 20,
        "id" : "number_items_heavy"
    }]


class Item(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    season = models.CharField(max_length=25, choices=SEASONS, default=SEASONS[0][1])
    activity = models.CharField(max_length=25, choices=ACTIVITIES, default=ACTIVITIES[0][1])
    age = models.CharField(max_length=25, choices=AGES, default=AGES[0][1])
    gender = models.CharField(max_length=25, choices=GENDERS, default=GENDERS[0][1])
    category = models.CharField(max_length=25, choices=CATEGORIES)
    trip_id = models.IntegerField(null=True)
    public = models.BooleanField(default=True)

    def __str__(self):
        return (f"{self.get_season_display()} on {self.name}")


class Vote(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    vote = models.IntegerField(default=0)
    checked = models.BooleanField(default=False)

    class Meta:
        ordering = ['-vote']


class Trip(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=25)
    country = models.CharField(max_length=25)
    date = models.DateField(default=datetime.now)
    season = models.CharField(max_length=25, choices=SEASONS, default=SEASONS[0][1])
    number_items = models.IntegerField(default=15)


class Activity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    activity = models.CharField(max_length=50, default=ACTIVITIES[0][1])


class Traveler(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=25)
    gender = models.CharField(max_length=25, choices=GENDERS, default=GENDERS[0][1])
    age = models.CharField(max_length=25, choices=AGES, default=AGES[0][1])


def getChoices(choices):
    return [x[1] for x in choices]
