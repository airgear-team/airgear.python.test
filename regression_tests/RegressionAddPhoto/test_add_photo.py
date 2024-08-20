import unittest

import requests

# URL для тестів
base_url = "http://localhost:8080"

# Bearer Token для автентифікації
bearer_token = "your_bearer_token"  # Замість "your_bearer_token" вставте реальний токен


class TestImage(unittest.TestCase):

    def test_add_image_without_auth(self):
        url = f"{base_url}/images/1"

        with open('earth.jpg', "rb") as image_file:
            files = {'images': ('earth.jpg', image_file, 'image/jpeg')}

            response = requests.post(url, files=files)

            # Перевіряємо, чи був повернутий очікуваний код статусу
            self.assertEqual(response.status_code, 404, f"Expected status code 404, but got {response.status_code}")

    def test_add_image_with_auth(self):
        url = f"{base_url}/images/1"
        with open('earth.jpg', 'rb') as image_file:
            files = {'images': ('earth.jpg', image_file, 'image/jpeg')}

            headers = {
                'Authorization': f'Bearer {bearer_token}'
            }

            response = requests.post(url, files=files, headers=headers)

            # Перевіряємо, чи був повернутий очікуваний код статусу
            self.assertEqual(response.status_code, 201, f"Expected status code 201, but got {response.status_code}")


#  TODO: Додавати може тільки той, хто створив товар

if __name__ == "__main__":
    unittest.main()
