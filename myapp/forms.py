# forms.py
from django import forms
from django.forms import formset_factory
from .models import Test, Question

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['subject', 'date']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['description', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option', 'answer_description']

QuestionFormSet = formset_factory(QuestionForm, extra=15)  
