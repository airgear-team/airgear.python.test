import unittest
import requests


class TestAuthenticateUser(unittest.TestCase):
    BASE_URL = "http://localhost:8080/auth"

    @classmethod
    def setUpClass(cls):
        print("\nПідготовка до тестування автентифікації...")

    def test_successful_authenticate_user(self):

        print("\nТестуємо успішну автентифікацію.")

        # Дані для аутентифікації зареєстрованого користувача
        auth_payload = {
            "email": "your_email", # Вставте правильну пошту замість your_email
            "password": "your_password" # Вставте правильний пароль замість your_password
        }

        headers = {
            'Content-Type': 'application/json'
        }

        print(f"Виконуємо POST-запит на URL: {self.BASE_URL}/authenticate, з правильними даними.")
        # Виконуємо POST-запит для аутентифікації
        response = requests.post(f"{self.BASE_URL}/authenticate", json=auth_payload, headers=headers)

        # Перевіряємо, що статус-код відповіді є 200 (OK)
        self.assertEqual(response.status_code, 200, "Expected status code 200, got {0}".format(response.status_code))

        # Перевіряємо, що у відповіді є токен
        response_data = response.json()
        self.assertIn("token", response_data, "Response JSON does not contain 'token'")
        print(f"\nАвтентифікація успішна, отримано токен: {response_data['token']}")


    def test_unsuccessful_authenticate_user(self):

        print("\nТестуємо безуспішну автентифікацію.")

        # Хибні дані для аутентифікації зареєстрованого користувача

        auth_payload = {
            "email": "wrong@email.com",  # правильну пошту
            "password": "all_wrong"  # неправильний пароль
        }

        headers = {
            'Content-Type': 'application/json'
        }

        print(f"Виконуємо POST-запит на URL: {self.BASE_URL}/authenticate, з хибними даними.")
        # Виконуємо POST-запит для аутентифікації
        response = requests.post(f"{self.BASE_URL}/authenticate", json=auth_payload, headers=headers)

        # Перевіряємо, що статус-код відповіді є 200 (OK)
        self.assertEqual(response.status_code, 401, "Expected status code 401, got {0}".format(response.status_code))

    def tearDown(self):
        print("Тест завершено.\n")


if __name__ == '__main__':
    unittest.main()
