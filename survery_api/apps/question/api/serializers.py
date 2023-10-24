import random
from django.shortcuts import get_object_or_404
from rest_framework.serializers import ModelSerializer, ValidationError

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
    options = QuestionOptionSerializer(many=True, required=False)

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

    def create(self, validated_data):
        question_type = validated_data.get("type")
        try:
            is_choice_type = ("radio" in question_type.code) or (
                "checkbox" in question_type.code
            )
            is_intuitive_type = "intuitive" in question_type.code

            response_text = validated_data.get("response_text")
            options_data = validated_data.pop("options", [])

            if (response_text and is_choice_type) or (
                len(options_data) and is_intuitive_type
            ):
                raise ValidationError("Invalid question type and response type")

            if (
                (is_choice_type and not len(options_data))
                or is_intuitive_type
                and not response_text
            ):
                raise ValidationError("A valid answer data is required")

            if is_choice_type:
                option_serializer = QuestionOptionSerializer(
                    data=options_data, many=True
                )
                option_serializer.is_valid(raise_exception=True)
                options = option_serializer.save()
                question = Question.objects.create(**validated_data)
                question.options.set(options)
                question.save()
                return question

            return super().create(validated_data)

        except Exception:
            raise ValidationError("Invalid question data")
