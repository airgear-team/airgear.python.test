import unittest
import requests

# URL для тестів
base_url = "http://localhost:8080"

# Bearer Token для автентифікації
bearer_token = "your_bearer_token" # Замість "your_bearer_token" вставте реальний токен


class TestGetPhotos(unittest.TestCase):

    def test_get_image_ids(self):
        url = f"{base_url}/images/1/images"

        headers = {
            'Authorization': f'Bearer {bearer_token}'
        }

        response = requests.get(url, headers=headers)

        self.assertEqual(response.status_code, 200, f"Expected status code 200, but got{response.status_code}")
        self.assertTrue(response.headers['Content-type'].startswith('application/json'), 'Response is not JSON')
