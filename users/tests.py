from django.test import TestCase

class UserTestCase(TestCase):
    databases={'default'}

    def setUp(self):
        self.create_token()
        self.create_test_data()


    def create_token(self):
        pass

    def create_test_data(self):
        pass