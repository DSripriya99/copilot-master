import unittest
from unittest.mock import patch
from main import app

class JokeTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('main.get_joke')
    def test_display_joke_valid_category(self, mock_get_joke):
        mock_get_joke.return_value = 'Why did the chicken cross the road? To get to the other side.'
        response = self.app.get('/display_joke/funny')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['joke'], 'Why did the chicken cross the road? To get to the other side.')

    def test_display_joke_invalid_category(self):
        response = self.app.get('/display_joke/invalid_category')
        self.assertEqual(response.status_code, 400)

    @patch('main.search_jokes')
    def test_search_joke_found(self, mock_search_jokes):
        mock_search_jokes.return_value = 'Why did the chicken go to the seance? To talk to the other side.'
        response = self.app.get('/search_joke/seance')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['joke'], 'Why did the chicken go to the seance? To talk to the other side.')

    @patch('main.search_jokes')
    def test_search_joke_not_found(self, mock_search_jokes):
        mock_search_jokes.return_value = 'No joke found.'
        response = self.app.get('/search_joke/nonexistent')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['joke'], 'No joke found.')

if __name__ == '__main__':
    unittest.main()