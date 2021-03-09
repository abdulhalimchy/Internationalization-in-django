from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from translated_fields import TranslatedFieldAdmin, to_attribute
from .models import Question

@admin.register(Question)
class QuestionAdmin(TranslatedFieldAdmin, admin.ModelAdmin):
    # # Pack question and answer fields into their own fieldsets:
    fieldsets = [
        (_("question"), {"fields": Question.question.fields}),
        (_("answer"), {"fields": Question.answer.fields}),
    ]

    # Show all fields in the changelist:
    list_display = [
        *Question.question.fields,
        *Question.answer.fields
    ]

    # Order by current language's question field:
    def get_ordering(self, request):
        return [to_attribute("question")]