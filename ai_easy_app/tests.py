from django.test import TestCase, Client
from django.http import JsonResponse

class AIBotViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_easy_endpoint(self):
        response = self.client.get('/ai_bot/easy/')
        self.assertEqual(response.status_code, 200)