from rest_framework import serializers

from .models import Entry

class EntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entry
        fields = ('id', 'entry_title', 'company')