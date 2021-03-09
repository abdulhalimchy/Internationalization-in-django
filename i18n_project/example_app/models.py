from django.db import models
from django.utils.translation import gettext_lazy as _
from translated_fields import TranslatedField

class Question(models.Model):
    
    question = TranslatedField(
        models.CharField(verbose_name=_("question"),max_length=200),
    )
    answer = TranslatedField(
        models.CharField(_("answer"), max_length=200),
    )

    def __str__(self):
        return self.question