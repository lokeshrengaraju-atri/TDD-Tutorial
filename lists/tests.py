from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page


class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        reponse = self.client.get("/")
        self.assertContains(reponse,"<title>To-Do lists</title>")
        self.assertContains(reponse, "<html>")
        self.assertContains(reponse, "/<html>")















