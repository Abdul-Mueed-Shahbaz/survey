from rest_framework.viewsets import ModelViewSet
from apps.question.api.serializers import QuestionSerializer, QuestionTypeSerializer
from apps.question.models import QuestionOption, QuestionType


class QuestionTypeViewSet(ModelViewSet):
    serializer_class = QuestionTypeSerializer
    queryset = QuestionType.objects.all().order_by("-created_on")
    permission_classes = []
    authentication_classes = []


class QuestionOptionViewSet(ModelViewSet):
    serializer_class = QuestionTypeSerializer
    queryset = QuestionOption.objects.all().order_by("-created_on")
    permission_classes = []
    authentication_classes = []


class QuestionViewSet(ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = QuestionOption.objects.all().order_by("-created_on")
    permission_classes = []
    authentication_classes = []
