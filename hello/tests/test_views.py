from django.test import TestCase, RequestFactory

from hello.views import index, game

class ViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index(self):
        request = self.factory.get('/')
        # response = index(request)
        # self.assertEqual(response.status_code, 200)

    def test_game(self):
        request = self.factory.get('/game/')
        # response = game(request)
        # self.assertEqual(response.status_code, 200)
