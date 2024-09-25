import unittest

import requests

class TestImage(unittest.TestCase):
    # URL для тестів
    BASE_URL = "http://localhost:8080"

    # Bearer Token для автентифікації
    BEARER_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJncmlpaWluNDEuZG9vZGU3MUBleGFtcGxlLmNvbSIsInJvbGVzIjoiUk9MRV9VU0VSIiwiaWF0IjoxNzI1ODk5MjkyLCJleHAiOjE3MjU5MTcyOTJ9.KwsFoMQ2dOdCwRn7JK9uBzXV5UrDvBA-CLXg9hmEcMw"  # Замість "your_bearer_token" вставте реальний токен

    def test_add_image_without_auth(self):
        url = f"{self.BASE_URL}/images/1"

        with open('earth.jpg', "rb") as image_file:
            files = {'images': ('earth.jpg', image_file, 'image/jpeg')}

            response = requests.post(url, files=files)

            # Перевіряємо, чи був повернутий очікуваний код статусу
            self.assertEqual(response.status_code, 404, f"Expected status code 404, but got {response.status_code}")

    def test_add_image_with_auth(self):
        url = f"{self.BASE_URL}/images/1"
        with open('earth.jpg', 'rb') as image_file:
            files = {'images': ('earth.jpg', image_file, 'image/jpeg')}

            headers = {
                'Authorization': f'Bearer {self.BEARER_TOKEN}'
            }

            response = requests.post(url, files=files, headers=headers)

            # Перевіряємо, чи був повернутий очікуваний код статусу
            self.assertEqual(response.status_code, 201, f"Expected status code 201, but got {response.status_code}")


#  TODO: Додавати може тільки той, хто створив товар

if __name__ == "__main__":
    unittest.main()
