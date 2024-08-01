import unittest
import requests


class TestRegisterUser(unittest.TestCase):
    BASE_URL = "http://localhost:8080/auth"

    def test_register_user(self):
        # Дані для реєстрації нового користувача
        register_payload = {
            "password": "secretpassword2",
            "email": "griiiin411.dode71@example.com",
            "phone": "+380151025644",
            "name": "test test"
        }

        headers = {
            'Content-Type': 'application/json'
        }

        # Виконуємо POST-запит для реєстрації
        response = requests.post(f"{self.BASE_URL}/register", json=register_payload, headers=headers)

        # Перевіряємо, що статус-код відповіді є 201 (OK), є вдалим, та призвів до створенню ресурсу
        self.assertEqual(response.status_code, 201, "Expected status code 201, got {0}".format(response.status_code))

        # Перевіряємо, що у відповіді є токен
        response_data = response.json()
        self.assertIn("token", response_data, "Response JSON does not contain 'token'")
        print(f"Registration successful, token received: {response_data['token']}")


if __name__ == '__main__':
    unittest.main()
