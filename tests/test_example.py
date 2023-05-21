from unittest import TestCase

from application import main


class TestExample(TestCase):
    def test_main_returns_true(self):
        self.assertTrue(main(), True)
