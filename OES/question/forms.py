from django import forms
from .models import Questions
class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['marks','question','choice1','choice2','choice3','choice4','answer']