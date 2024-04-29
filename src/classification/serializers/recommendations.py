# -*- coding: utf-8 -*-#
from rest_framework import serializers

from classification.models import Recommendations


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendations
        fields = ["content", "created_at"]
