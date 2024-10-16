import json

from django.http import JsonResponse
from django.test import TestCase, RequestFactory

from .puzzle import is_valid
from .views import puzzle


class PuzzleTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_puzzle(self):
        request = self.factory.get('/puzzle')
        response = puzzle(request)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)

        data = json.loads(response.content)
        self.assertGreaterEqual(data['n_attempts'], 0)
        self.assertTrue(is_valid(data['puzzle']))
