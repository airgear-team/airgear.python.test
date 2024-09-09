import unittest

import requests


class TestUpdateGoods(unittest.TestCase):
    # Базовий URL для API
    BASE_URL = "http://localhost:8080/goods/1"

    # Вставте свій bearer token тут
    AUTH_TOKEN = "your_bearer_token_here"

    @classmethod
    def setUpClass(cls):
        print("\nПідготовка до тестування оновлення товару...")

    def test_successful_update(self):
        print("\nТестуємо успішне оновлення товару...")
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

        print(f"Виконуємо PUT-запит на URL: {self.BASE_URL} з payload: {payload}")
        response = requests.put(self.BASE_URL, json=payload, headers=headers)

        # Перевіряємо відповідь сервера
        print(f"Отримано відповідь з кодом статусу: {response.status_code}")
        self.assertEqual(200, response.status_code, f'Expected status code 200, but {response.status_code} got')

    def test_wrong_update(self):
        print(f"\nТестуємо безуспішне оновлення товару")
        # Немає name та description
        payload = {
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

        print(f"Виконуємо PUT-запит на URL: {self.BASE_URL} з payload: {payload}")
        response = requests.put(self.BASE_URL, json=payload, headers=headers)

        # Перевіряємо відповідь сервера
        print(f"Отримано відповідь з кодом статусу: {response.status_code}")
        self.assertEqual(400, response.status_code, f'Expected status code 200, but {response.status_code} got')

    def tearDown(self):
        print("Тест завершено.\n")


if __name__ == "__main__":
    unittest.main()
