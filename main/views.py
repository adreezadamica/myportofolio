from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience
from main.forms import ExperienceForm


def show_main(request):
    context = {
        "name": "Damica Adreeza Ramadhan",
        "npm": "2506625193",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "A freshman passionate about mathematics, logical reasoning, and technology."
            "My ability to quickly adapt and see new challenges as opportunities for growth makes me an eager self-starter."
            "I am driven to apply my skills in an environment where I can contribute to and learn from a successful team."
        ),
    }
    return render(request, "index.html", context)

def show_experience(request):
    json_response = get_experiences_json(request)

    deserialized_data = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    experiences = [item.object for item in deserialized_data]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Damica",
        "experience_list": experiences,
        "title_query": title_query,
    }

    return render(request, "experience.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Damica",
        "form": form,
    }

    return render(request, "experience_form.html", context)

def get_experiences_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")