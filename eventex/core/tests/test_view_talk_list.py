from django.test import TestCase
from django.shortcuts import resolve_url as r

from eventex.core.models import Talk, Speaker


class TalkListGet(TestCase):
    def setUp(self):
        t1 = Talk.objects.create(
            title='Título da Palestra',
            start='10:00',
            description='Descrição da palestra.'
        )
        t2 = Talk.objects.create(
            title='Título da Palestra',
            start='13:00',
            description='Descrição da palestra.'
        )
        speaker = Speaker.objects.create(
            name='Rafael Correia',
            slug='rafael-correia',
            website='http://blog.abraseucodigo.com.br'
        )
        t1.speakers.add(speaker)
        t2.speakers.add(speaker)

        self.resp = self.client.get(r('talk_list'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/talk_list.html')

    def test_html(self):
        contents = [
            (2, 'Título da Palestra'),
            (1, '13:00'),
            (1, '10:00'),
            (2, '/palestrantes/rafael-correia/'),
            (2, 'Rafael Correia'),
            (2, 'Descrição da palestra.'),
        ]
        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected, count)

    def test_context(self):
        variables = ['morning_talks', 'afternoon_talks']
        for key in variables:
            with self.subTest():
                self.assertIn(key, self.resp.context)


class TalkListGetEmpty(TestCase):
    def test_get_empty(self):
        resp = self.client.get(r('talk_list'))
        self.assertContains(resp, 'Ainda não existem palestras de manhã.')
        self.assertContains(resp, 'Ainda não existem palestras de tarde.')
