import random
from .models import Item, Vote, SEASONS, ACTIVITIES, AGES, GENDERS, CATEGORIES, getChoices
from django.contrib.auth.models import User
from .static.data.places import select_cities, cities, presentation_cities
from .static.data.items import item_names, categorized_items
from .static.data.people import first_names, last_names


season_choices = getChoices(SEASONS)
activity_choices = getChoices(ACTIVITIES)
age_choices = getChoices(AGES)
gender_choices = getChoices(GENDERS)
category_choices = getChoices(CATEGORIES)


def generateItemData(n):
    data = []
    for i in range(n):
        random_city = presentation_cities[random.randint(0, len(presentation_cities)-1)]

        random_category = category_choices[random.randint(0, len(category_choices)-1)]
        category_list = categorized_items[random_category]
        random_item = category_list[random.randint(0, len(category_list)-1)]

        item = Item.objects.create(
            name=random_item.title(),
            city=random_city["City"].title(),
            country=random_city["Country"].title(),
            season=season_choices[random.randint(0, len(season_choices)-1)].title(),
            activity=activity_choices[random.randint(0, len(activity_choices)-1)].title(),
            age=age_choices[random.randint(0, len(age_choices)-1)].title(),
            gender=gender_choices[random.randint(0, len(gender_choices)-1)].title(),
            category=random_category,
            trip_id=None
        )
        item.save()
        name = item_names[random.randint(0, len(item_names)-1)]
        city = random_city["City"]
        country = random_city["Country"]
        data.append({
            i, name, city, country
        })
    return data


def generateUserData(n):
    data = []
    fn_length = len(first_names)
    ln_length = len(last_names)

    for i in range(n):
        name = first_names[random.randint(0, fn_length-1)]
        last_name = last_names[random.randint(0, ln_length-1)]["last_name"]
        first_name = name["first_name"]
        user = User.objects.create(
            username=first_name + last_name + str(random.randint(0, 999)),
            first_name=first_name,
            last_name=last_name,
        )
        user.save()

        data.append({
            first_name, last_name
        })
    return data


def generateVoteData(n):
    data = []
    items = Item.objects.all()
    users = User.objects.all()

    items_length = len(items)
    users_length = len(users)
    for i in range(n):
        item = items[random.randint(0, items_length-1)]
        user = users[random.randint(0, users_length-1)]
        score = round((random.randint(-100, 100) + 30)/100)
        if len(Vote.objects.filter(user=user, item=item)) > 0:
            # print("%s || already exists" % (i))
            pass
        else:
            vote = Vote.objects.create(
                user=user,
                item=item,
                vote=score
            )
            vote.save()
            # print("%s || creating object" % (i))

            data.append({
                item, user, score
            })
    print(len(data))

    # print(items[random.randint(0, items_length-1)], users[random.randint(0, users_length)])

    return data
