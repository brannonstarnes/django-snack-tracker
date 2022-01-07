from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Snack(models.Model):
    name = models.CharField(max_length=64)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(max_length=256)

    def __str__(self):  
        return self.name

    def get_absolute_url(self):
        return reverse('detail_view', args=[str(self.id)])


#DONE add purchaser ForeignKey related to Django’s built in user model with CASCADE delete option.
# DONE from django.contrib.auth import get_user_model
# DONE add description TextField
# DONE add model to admin
# DONE modify Snack model have user friendly display in admin
# DONE create migrations and migrate data
# DONE create a super user
# DONE run development server

# DONE DONT FORGET TO MIGRATE MODELS AFTER CREATED with manage.py migrate