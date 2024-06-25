import unittest
from unittest.mock import patch
from joke import get_joke, search_jokes

class JokeTestCase(unittest.TestCase):
    @patch('joke.requests.get')
    def test_get_joke_single(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'type': 'single',
            'joke': 'Why did the chicken cross the road? To get to the other side.'
        }
        result = get_joke('Programming', 'nsfw,religious')
        self.assertEqual(result, 'Why did the chicken cross the road? To get to the other side.')

    @patch('joke.requests.get')
    def test_get_joke_twopart(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'type': 'twopart',
            'setup': 'Why did the chicken cross the road?',
            'delivery': 'To get to the other side.'
        }
        result = get_joke('Programming', 'nsfw,religious')
        self.assertEqual(result, 'Why did the chicken cross the road? - To get to the other side.')

    @patch('joke.requests.get')
    def test_get_joke_no_joke(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        result = get_joke('Programming', 'nsfw,religious')
        self.assertEqual(result, 'No joke found.')

    @patch('joke.requests.get')
    def test_search_jokes_found(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'type': 'single',
            'joke': 'Why did the chicken go to the seance? To talk to the other side.'
        }
        result = search_jokes('seance')
        self.assertEqual(result, 'Why did the chicken go to the seance? To talk to the other side.')

    @patch('joke.requests.get')
    def test_search_jokes_not_found(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        result = search_jokes('seance')
        self.assertEqual(result, 'No joke found.')

if __name__ == '__main__':
    unittest.main()