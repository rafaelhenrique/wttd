from eventex.core.models import Talk

from django.test import TestCase


class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title='Título da Palestra',
        )

    def test_create(self):
        self.assertTrue(Talk.objects.exists())

    def test_has_speakers(self):
        """Talk has many Speakers and vice-versa"""
        self.talk.speakers.create(
            name='Rafael Correia',
            slug='rafael-correia',
            website='http://blog.abraseucodigo.com.br',
        )
        self.assertEqual(1, self.talk.speakers.count())

    def test_fields_can_be_blank(self):
        fields = ('start', 'description', 'speakers')
        for field in fields:
            with self.subTest():
                field = Talk._meta.get_field(field)
                self.assertTrue(field.blank)

    def test_start_null(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.null)

    def test_str(self):
        self.assertEqual('Título da Palestra', str(self.talk))
