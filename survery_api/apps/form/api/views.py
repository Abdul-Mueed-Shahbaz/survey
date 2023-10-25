from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.form.api.serializers import FormSerializer
from apps.form.models import Form
from rest_framework.decorators import action

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
        methods=["GET"],
        url_path="add_question",
        url_name="Add Question To Form",
    )
    def add_question_to_form(self, request):
        # form = self.get_object()
        # questions = request.data.get("questions")
        # question =
        return Response(status=status.HTTP_200_OK)
