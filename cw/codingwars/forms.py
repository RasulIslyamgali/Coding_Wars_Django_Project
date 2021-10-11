from .models import SubjectNames, Uroki
from django.forms import ModelForm, TextInput, Textarea, ModelChoiceField
import widget_tweaks


class SubjectNamesForm(ModelForm):
    class Meta:
        model = SubjectNames
        fields = ["subject_name", 'subject_description',]

        widgets = {
            "subject_name": TextInput(attrs={
                "class": "form-control",
                "style": "width: 400px;",
                "placeholder": "Язык программирования",
            }),
            "subject_description": Textarea(attrs={
                "class": "form-control",
                "style": "width: 400px;",
                "align": "center",
                "placeholder": "Описание",
            }),
        }


class UrokiForm(ModelForm):
    class Meta:
        model = Uroki
        fields = ["urok_name", 'urok_description', "urok_text", "subject"]
        # subjects = ModelChoiceField(queryset=SubjectNames.objects.all())
        subject = ModelChoiceField(queryset=SubjectNames.objects.all(), empty_label="Выберите раздел")
        widgets = {
            "urok_name": TextInput(attrs={
                "class": "form-control",
                "style": "width: 400px;",
                "placeholder": "Название урока",
            }),
            "urok_description": TextInput(attrs={
                "class": "form-control",
                "style": "width: 400px; height: 100",
                "align": "center",
                "placeholder": "Краткое описание",
            }),
            "urok_text": Textarea(attrs={
                "class": "form-control",
                "style": "width: 400px;",
                "align": "center",
                "placeholder": "Текст",
            }),
        }


