import json

from django.http import JsonResponse
from django.test import TestCase, RequestFactory

from .puzzle import is_valid
from .views import puzzle


class PuzzleTestCase(TestCase):
    def setUp(self):
        """Set up the test case with a RequestFactory instance."""
        self.factory = RequestFactory()

    def test_puzzle(self):
        """Test the puzzle view to ensure it returns a valid Sudoku puzzle."""
        # Create a GET request to the '/puzzle' endpoint
        request = self.factory.get('/puzzle')

        # Call the puzzle view with the request
        response = puzzle(request)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Ensure the response is an instance of JsonResponse
        self.assertIsInstance(response, JsonResponse)

        # Load the JSON data from the response content
        data = json.loads(response.content)

        # Check that the number of attempts is greater than or equal to 0
        self.assertGreaterEqual(data['n_attempts'], 0)

        # Validate the generated Sudoku puzzle
        self.assertTrue(is_valid(data['puzzle']))
