from django.conf import settings
from django.db import models
from django.utils import timezone


class Entry(models.Model):
    entry_title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    trophy_names = models.TextField(blank=True, null=True)
    is_winner = models.BooleanField()
    audience_honor = models.BooleanField()
    category = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    street_address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.PositiveIntegerField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    is_individual = models.BooleanField()
    is_organization = models.BooleanField()
    company = models.CharField(max_length=255, blank=True, null=True)
    image = models.URLField(max_length=255, blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.entry_title