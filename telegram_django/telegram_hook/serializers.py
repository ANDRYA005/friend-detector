from rest_framework import serializers

from telegram_hook.models import Person


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ("id", "name", "created")
