from django import forms
from .models import *

class QuestionForm(forms.Form):

    DEMO_CHOICES = (
    ("1", "choice 1"),
    ("2", "choice 2"),
    )

    question = forms.MultipleChoiceField(choices = DEMO_CHOICES)

    # def __init__(self, *args, **kwargs):
    #     answer_choices = kwargs.pop('answer_choices', ())
    #     super().__init__(*args, **kwargs)
    #     self.fields['answer'].choices = answer_choices

