# -*- coding: utf-8 -*-#
from rest_framework import serializers

from home.models import ContactMessages


class ContactMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessages
        fields = ["first_name", "last_name", "email", "phone", "message"]
