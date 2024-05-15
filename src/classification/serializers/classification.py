# -*- coding: utf-8 -*-#
from rest_framework import serializers

from classification.models import Classification
from classification.serializers.recommendations import RecommendationSerializer


class ClassificationSerializer(serializers.ModelSerializer):
    recommendations = RecommendationSerializer(read_only=True, many=True)

    class Meta:
        model = Classification
        fields = [
            "id",
            "label",
            "slug",
            "created_at",
            "recommendations",
            "description",
            "classification_number",
            "is_enabled",
            "short_advice",
            "conclusion_advice",
            "image",
        ]
        depth = 1
