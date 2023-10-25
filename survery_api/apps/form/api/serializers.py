from rest_framework.serializers import ModelSerializer
from apps.form.models import Form
from apps.question.api.serializers import QuestionSerializer


class FormSerializer(ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Form
        fields = "__all__"
