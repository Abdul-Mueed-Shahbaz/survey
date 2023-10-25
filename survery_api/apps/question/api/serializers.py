from functools import partial
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

    def get_choice_type(self, type_instance):
        is_choice_type = ("radio" in type_instance.code) or (
            "checkbox" in type_instance.code
        )
        is_intuitive_type = "intuitive" in type_instance.code
        return is_choice_type, is_intuitive_type

    def update(self, instance, validated_data):
        # TODO: Handle Options Data updation Later
        validated_data.pop("options", [])
        return super().update(instance, validated_data)

    def validate(self, attrs):
        question_type = attrs.get("type")
        is_choice_type, is_intuitive_type = self.get_choice_type(question_type)

        response_text = attrs.get("response_text")
        options_data = attrs.get("options", [])

        if (response_text and is_choice_type) or (
            len(options_data) and is_intuitive_type
        ):
            raise ValidationError("Invalid question type and response type")

        if (
            (is_choice_type and len(options_data) < 2)
            or is_intuitive_type
            and not response_text
        ):
            raise ValidationError("A valid user response data is required")

        return attrs

    def create(self, validated_data):
        question_type = validated_data.get("type")
        try:
            is_choice_type, _ = self.get_choice_type(question_type)

            if is_choice_type:
                option_serializer = QuestionOptionSerializer(
                    data=validated_data.pop("options", []), many=True
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
