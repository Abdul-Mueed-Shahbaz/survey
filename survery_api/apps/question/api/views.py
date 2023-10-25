from rest_framework.viewsets import ModelViewSet
from apps.question.api.serializers import (
    QuestionOptionSerializer,
    QuestionSerializer,
    QuestionTypeSerializer,
)
from apps.question.models import Question, QuestionOption, QuestionType


class QuestionTypeViewSet(ModelViewSet):
    serializer_class = QuestionTypeSerializer
    queryset = QuestionType.objects.filter(is_deleted=False, is_active=True).order_by(
        "-created_on"
    )
    permission_classes = []
    authentication_classes = []
    lookup_field = "code"


class QuestionOptionViewSet(ModelViewSet):
    serializer_class = QuestionOptionSerializer
    queryset = QuestionOption.objects.filter(is_deleted=False, is_active=True).order_by(
        "-created_on"
    )
    permission_classes = []
    authentication_classes = []


class QuestionViewSet(ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.filter(is_deleted=False, is_active=True).order_by(
        "-created_on"
    )
    permission_classes = []
    authentication_classes = []
    http_method_names = ["get", "delete", "post", "patch", "put"]
