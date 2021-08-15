from django.shortcuts import render

from rest_framework import viewsets

from .serializers import EntrySerializer
from .models import Entry


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all().order_by('entry_title')
    serializer_class = EntrySerializer