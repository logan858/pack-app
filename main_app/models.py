from django.db import models
from django.contrib.auth.models import User





# City Model
class City(models.Model):
    city_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    def __str__(self):
        return self.city_name

    def get_absolute_url(self):
        return reverse('searched_city', kwargs={'pk': self.id})

# Seasons
season = (
    ('WT', 'Winter'),
    ('SP', 'Spring'),
    ('SM', 'Summer'),
    ('FL', 'Fall'),
)

activity = (
    ('Au', 'Austin'),
    ('Lo', 'Logan'),
    ('Da', 'Daniel'),
    ('Mi', 'Mike'),
    ('Ma', 'Marielle'),
    ('Mi', 'Shirley'),
)

class Item (models.Model):
    name = models.CharField(max_length=50)
    season = models.CharField(
    max_length=2,
    choices= season,
    default= season[0][0],
    )
    activity =  models.CharField(
        max_length=2,
        choices= activity,
        default=activity[0][0],
    )
    vote = models.IntegerField(
        default = 0
    )
    # 1:M model, establishing the foreign key
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    
    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return (f"{self.get_season_display()} on {self.name}")

    # sort by voting
    class Meta:
        ordering = ['-vote']

    # create the M:M
    user = models.ManyToManyField(User)

    # Link the user
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

