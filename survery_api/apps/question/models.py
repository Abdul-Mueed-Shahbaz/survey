from django.db.models import (
    CharField,
    ForeignKey,
    ImageField,
    BooleanField,
    ManyToManyField,
    TextField,
    CASCADE,
)
from django.core.exceptions import ValidationError
from apps.common.models import BaseModel


def image_upload(instance, filename):
    return f"images/questions/{filename}"


# Create your models here.
class QuestionType(BaseModel):
    name = CharField(max_length=255, null=False, blank=False)
    code = CharField(max_length=255, null=False, blank=False)

    class Meta:
        db_table = "question_type"


class QuestionOption(BaseModel):
    option_text = CharField(max_length=255)
    is_correct = BooleanField(default=False)

    class Meta:
        db_table = "question_option"


class Question(BaseModel):
    image = ImageField(upload_to=image_upload, blank=True, null=True)
    type = ForeignKey(QuestionType, blank=False, null=False, on_delete=CASCADE)
    statement = TextField(null=False, blank=False)
    response_text = TextField(blank=True, null=True)
    options = ManyToManyField(QuestionOption, blank=True)

    class Meta:
        db_table = "question"

    def clean(self):
        is_choice_type = "choice" in self.type.name.lower()
        is_intuitive_type = "intuitive" in self.type.name.lower()

        if (self.response_text and is_choice_type) or (
            self.options.exists() and is_intuitive_type
        ):
            raise ValidationError("Invalid question type and response type")

        if (
            (is_choice_type and not self.options.exists())
            or is_intuitive_type
            and not self.response_text
        ):
            raise ValidationError("A valid response is required")

        super().clean()
