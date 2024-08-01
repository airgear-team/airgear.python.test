import unittest
import requests


class TestAuthenticateUser(unittest.TestCase):
    BASE_URL = "http://localhost:8080/auth"

    def test_authenticate_user(self):
        # Дані для аутентифікації зареєстрованого користувача
        auth_payload = {
            "email": "griiiin41.dode71@example.com",
            "password": "secretpassword2"
        }

        headers = {
            'Content-Type': 'application/json'
        }

        # Виконуємо POST-запит для аутентифікації
        response = requests.post(f"{self.BASE_URL}/authenticate", json=auth_payload, headers=headers)

        # Перевіряємо, що статус-код відповіді є 200 (OK)
        self.assertEqual(response.status_code, 200, "Expected status code 200, got {0}".format(response.status_code))

        # Перевіряємо, що у відповіді є токен
        response_data = response.json()
        self.assertIn("token", response_data, "Response JSON does not contain 'token'")
        print(f"Authentication successful, token received: {response_data['token']}")


if __name__ == '__main__':
    unittest.main()
