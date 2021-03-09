from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    """
    Serializes the Question object
    """

    class Meta:
        model = Question
        fields = ['pk', 'question', 'answer']