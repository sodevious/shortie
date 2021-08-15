import data_wizard
from .models import Entry
from rest_framework import serializers


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'

        # Optional - see options below
        data_wizard = {
            'header_row': 0,
            'start_row': 1,
            'show_in_list': True,
            'idmap': data_wizard.idmap.existing,
        }

# Use default name & serializer
data_wizard.register(Entry)
