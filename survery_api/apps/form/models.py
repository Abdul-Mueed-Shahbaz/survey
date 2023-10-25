from django.db.models import CharField, ManyToManyField

from apps.common.models import BaseModel
from apps.question.models import Question


# Create your models here.
class Form(BaseModel):
    title = CharField(max_length=255, null=False, blank=False)
    description = CharField(max_length=1000, null=False, blank=False)
    questions = ManyToManyField(Question, blank=True)

    class Meta:
        db_table = "form"
