from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Experience

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
        ]

        labels = {
            "title": "Pengalaman Yang Dijalani",
            "description": "Deskripsi Pengalaman",
            "category": "Kategori Pengalaman",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Menjadi Panitia Acara",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Peranmu",
                    "rows": 3,
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "Full-Time, Part-Time, Internship, Freelance",
                }
            ),
        }