from django.test import TestCase
from .models import Characteristic


class CharacteristicApiTests(TestCase):
    def test_characteristics_endpoint_exists_and_returns_data(self):
        Characteristic.objects.create(name='Attacking')
        Characteristic.objects.create(name='Balanced')

        response = self.client.get('/characteristics/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        self.assertIn('Attacking', [item['name'] for item in response.json()])
