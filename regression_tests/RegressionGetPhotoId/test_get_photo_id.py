import unittest
import requests

# URL для тестів
base_url = "http://localhost:8080"

# Bearer Token для автентифікації
bearer_token = "your_bearer_token"  # Замість "your_bearer_token" вставте реальний токен


class TestGetPhotos(unittest.TestCase):

    def test_get_image_ids(self):
        url = f"{base_url}/images/1/images"

        headers = {
            'Authorization': f'Bearer {bearer_token}'
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

    def get_image_by_id(self):

        image_ids = [
            "4537ab99-6652-4c79-a207-cc91c87c4fb2",
            "2a59abd9-6fa9-4605-80cd-7381ce98e90d",
            "53d0292e-cf2e-4896-bd49-4823d83fe8cd"
        ]

        for image_id in image_ids:
            url = f"{base_url}/images/{image_id}.jpg"

            headers = {
                'Authorization': f'Bearer {bearer_token}'
            }

            response = requests.get(url, headers=headers)

            # Перевірка на очікуваний код статусу
            self.assertEqual(response.status_code, 200, f'Expected 200, but got {response.status_code}')


if __name__ == "__main__":
    unittest.main()
