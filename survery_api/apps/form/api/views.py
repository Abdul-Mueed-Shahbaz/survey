from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.form.api.serializers import FormSerializer
from apps.form.models import Form
from rest_framework.decorators import action

from apps.question.api.serializers import QuestionSerializer
from apps.question.models import Question

# Create your views here.


class FormViewSet(ModelViewSet):
    serializer_class = FormSerializer
    queryset = Form.objects.filter(is_deleted=False, is_active=True).order_by(
        "-created_on"
    )
    permission_classes = []
    authentication_classes = []

    @action(
        detail=True,
        methods=["POST"],
        url_path="add-question",
        url_name="Add Question To Form",
    )
    def add_question_to_form(self, request, pk):
        form = self.get_object()
        question_ids = request.data.get("questions")
        if question_ids:
            questions_qs = Question.objects.filter(id__in=question_ids)
            if len(questions_qs) == len(question_ids):
                form.questions.add(*questions_qs)
            else:
                raise ValidationError("Incorrect Question Attached")
        else:
            raise ValidationError("Question Ids are required")

        return Response(
            {"message": "Question added successfully"}, status=status.HTTP_201_CREATED
        )
