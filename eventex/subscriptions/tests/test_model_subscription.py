from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def test_create(self):
        obj = Subscription(
            name='Rafael Henrique da Silva Correia',
            cpf='12345678901',
            email='rafael@abraseucodigo.com.br',
            phone='00-90000-9000',
        )
        obj.save()
        self.assertTrue(Subscription.objects.exists())
