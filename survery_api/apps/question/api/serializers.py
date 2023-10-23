from rest_framework.serializers import ModelSerializer

from apps.question.models import Question, QuestionOption, QuestionType


class QuestionTypeSerializer(ModelSerializer):
    class Meta:
        model = QuestionType
        fields = "__all__"


class QuestionOptionSerializer(ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = "__all__"


class QuestionSerializer(ModelSerializer):
    options = QuestionOptionSerializer(many=True)

    class Meta:
        model = Question
        fields = [
            "id",
            "image",
            "type",
            "statement",
            "response_text",
            "options",
        ]
