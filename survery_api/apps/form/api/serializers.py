from rest_framework.serializers import ModelSerializer
from apps.form.models import Form


class FormSerializer(ModelSerializer):
    class Meta:
        model = Form
        fields = "__all__"
