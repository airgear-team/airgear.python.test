import unittest
import requests


class TestGetPhotos(unittest.TestCase):
    # URL для тестів
    BASE_URL = "http://localhost:8080"

    # Bearer Token для автентифікації
    BEARER_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJncmlpaWluNDEuZG9vZGU3MUBleGFtcGxlLmNvbSIsInJvbGVzIjoiUk9MRV9VU0VSIiwiaWF0IjoxNzI1ODk5MjkyLCJleHAiOjE3MjU5MTcyOTJ9.KwsFoMQ2dOdCwRn7JK9uBzXV5UrDvBA-CLXg9hmEcMw"  # Замість "your_bearer_token" вставте реальний токен

    @classmethod
    def setUpClass(cls):
        print("\nТестування почато.")

    def test_get_image_ids(self):
        url = f"{self.BASE_URL}/images/1/images"

        headers = {
            'Authorization': f'Bearer {self.BEARER_TOKEN}'
        }

        response = requests.get(url, headers=headers)

        # Перевірка, чи повернутий очікуваний код статусу
        self.assertEqual(response.status_code, 200, f"Expected status code 200, but got{response.status_code}.")
        # Перевірка, чи відповідь у форматі JSON
        self.assertTrue(response.headers['Content-type'].startswith('application/json'), 'Response is not JSON.')
        response_data = response.json()
        self.assertGreater(len(response_data), 0, "Response JSON is empty.")

        for image in response_data:
            self.assertIn('imageUrl', image, "Missing 'imageUrl' in response JSON.")

    def test_get_image_by_id(self):

        # Требеа замінити IDшки, та перед цим тестом виконати RegressionAddPhoto/test_add_photo.py
        image_ids = [
            "4537ab99-6652-4c79-a207-cc91c87c4fb2",
            "2a59abd9-6fa9-4605-80cd-7381ce98e90d",
            "53d0292e-cf2e-4896-bd49-4823d83fe8cd"
        ]

        for image_id in image_ids:
            url = f"{self.BASE_URL}/images/{image_id}.jpg"

            headers = {
                'Authorization': f'Bearer {self.BEARER_TOKEN}'
            }

            response = requests.get(url, headers=headers)

            # Перевірка на очікуваний код статусу
            self.assertEqual(response.status_code, 200, f'Expected 200, but got {response.status_code}.')
            # Перевірка чи відповідь містить зображення (перевірка на тип 'image')
            self.assertTrue(response.headers['Content-type'].startswith('images/'),
                            f"Response for {image_id} is not an image.")


if __name__ == "__main__":
    unittest.main()
