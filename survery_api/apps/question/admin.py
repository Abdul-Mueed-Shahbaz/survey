from django.contrib import admin

from apps.question.models import Question, QuestionOption, QuestionType

# Register your models here.
admin.site.register([Question, QuestionType, QuestionOption])
