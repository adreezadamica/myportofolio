from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience


class MainTest(TestCase):
    def setUp(self):
        self.exp1 = Experience.objects.create(
            title="Staff Marketing of COMPFEST 18",
            description="promote the event directly (done while MC), create content, and share broadcasts.",
            category="part-time",
        )

        self.exp2 = Experience.objects.create(
            title="Staff of Departemen Akademik dan Profesi BEM Fasilkom UI 2026",
            description="Facilitating students in academic and career development, such as holding joint study mentoring, seminars, and sharing internship and scholarship information.",
            category="part-time",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.exp1.title)
        self.assertNotContains(response, self.exp2.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.exp1), "Staff Marketing of COMPFEST 18")
        self.assertEqual(self.exp1.category, "part-time")
        self.assertTrue(self.exp1.is_ongoing)

        self.assertEqual(str(self.exp2), "Staff of Departemen Akademik dan Profesi BEM Fasilkom UI 2026")
        self.assertEqual(self.exp2.category, "part-time")
        self.assertTrue(self.exp2.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")

        self.assertEqual(len(response.context["experience_list"]), 2)

        self.assertContains(response, self.exp1.title)
        self.assertContains(response, self.exp1.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Ongoing")

        self.assertContains(response, self.exp2.title)
        self.assertContains(response, self.exp2.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Ongoing")
        
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        now = timezone.now()
        self.exp1.ended_at = now
        self.exp1.save()

        self.exp2.ended_at = now
        self.exp2.save()

        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.exp1.is_ongoing)
        self.assertFalse(self.exp2.is_ongoing)
        
        self.assertContains(response, "Done")
        self.assertNotContains(response, "Ongoing")