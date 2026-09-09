from django.shortcuts import render

from main.models import Experience


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
    context = {
        "name": "Damica",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)