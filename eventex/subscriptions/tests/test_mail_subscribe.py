from django.test import TestCase
from django.core import mail
from django.shortcuts import resolve_url as r


class SubscribeEmail(TestCase):
    def setUp(self):
        data = dict(
            name='Rafael Henrique da Silva Correia', cpf='12345678901',
            email='rafael@abraseucodigo.com.br', phone='00-90000-9000')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'rafael@abraseucodigo.com.br']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Rafael Henrique da Silva Correia',
            '12345678901',
            'rafael@abraseucodigo.com.br',
            '00-90000-9000'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
