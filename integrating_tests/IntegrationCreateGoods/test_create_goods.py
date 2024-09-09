import unittest
import requests


class TestCreateGoods(unittest.TestCase):
    BASE_URL = "http://localhost:8080/goods/"
    AUTH_TOKEN = "your_auth_token_here"  # Замість "your_auth_token_here" вставте реальний токен

    @classmethod
    def setUpClass(cls):
        print("\nПідготовка до тестування створення товару...")

    def test_create_goods(self):
        print("\nТестуємо успішне створення товару...")
        # Дані для створення товару
        payload = {
            "name": "Valid Product Name",  # Оновлений name
            "description": "This is a valid description with more than 10 characters.",  # Оновлений description
            "price": {
                "priceAmount": "123.00",  # Переконуємось, що формат BigDecimal коректний
                "priceCurrency": "USD",
                "priceType": "NEGOTIATED_PRICE"
            },
            "weekendsPrice": {
                "weekendsPriceAmount": "1234.00",  # Переконуємось, що формат BigDecimal коректний
                "weekendsPriceCurrency": "USD",
                "weekendsPriceType": "NON_NEGOTIATED_PRICE"
            },
            "deposit": {
                "depositAmount": "1234.00",  # Переконуємось, що формат BigDecimal коректний
                "depositCurrency": "USD",
                "depositPriceType": "NON_NEGOTIATED_PRICE"
            },
            "locationId": 121,  # Переконуємось, що тип Long коректний
            "category": {
                "id": 1,  # Переконуємось, що тип Integer коректний
                "name": "Category Name"  # Додаємо ім'я категорії
            },
            "phoneNumber": "+380934343454",
            "goodsCondition": "NEW"
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.AUTH_TOKEN}'  # Додаємо заголовок авторизації
        }

        print(f"Виконуємо POST-запит на URL: {self.BASE_URL} з payload: {payload}")
        # Виконуємо POST-запит
        response = requests.post(self.BASE_URL, json=payload, headers=headers)

        print(f"Отримано відповідь з кодом статусу: {response.status_code}")

        # Якщо відповідь не є 201, виводимо її для діагностики
        if response.status_code != 201:
            print(f"Response status code: {response.status_code}")
            print(f"Response content: {response.content.decode()}")

        # Перевіряємо, що статус-код відповіді є 201 (Created)
        self.assertEqual(response.status_code, 201, "Expected status code 201, got {0}".format(response.status_code))

        # Перевіряємо тіло відповіді
        response_data = response.json()
        self.assertIn("id", response_data, "Response JSON does not contain 'id'")
        self.assertEqual(response_data["name"], payload["name"], "Response 'name' does not match")

        # Додаткові перевірки можна додати за потребою

    def tearDown(self):
        print("Тест завершено.\n")


if __name__ == '__main__':
    unittest.main()
