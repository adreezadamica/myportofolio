from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Experience
from main.models import Projects

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

class ProjectsForm(ModelForm):
    class Meta:
        model = Projects
        fields = [
            "title",
            "description",
            "category",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "category": "Kategori Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Contoh: Website Portofolio Pribadi",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan peran atau fitur di proyekmu",
                    "rows": 3,
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "web, mobile, ai-ml, robotics",
                }
            ),
        }