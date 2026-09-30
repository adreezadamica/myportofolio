from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Experience
from main.models import Projects

from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

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
        fields = ["title", "description", "category", "thumbnail"]
        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "category": "Kategori Proyek",
            "thumbnail": "URL Thumbnail (opsional)",
        }
        widgets = {
            "title": TextInput(attrs={"placeholder": "Contoh: Website Portofolio Pribadi", "maxlength": 255}),
            "description": Textarea(attrs={"placeholder": "Ceritakan peran atau fitur di proyekmu", "rows": 3}),
            "thumbnail": URLInput(attrs={"placeholder": "https://contoh.com/gambar.jpg"}),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()