from unittest import TestCase
from setup_classes import Connection, Session


class Setup2TestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.connection = Connection()

    @classmethod
    def tearDownClass(cls):
        cls.connection.close()

    def setUp(self):
        self.session = Session()

    def tearDown(self):
        self.session.close()

    def test_db_acess_save(self):
        """"Test db save"""
        print('### Running save')

    def test_db_acess_delete(self):
        """"Test db deletion"""
        print('### Running delete')