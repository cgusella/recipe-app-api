from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""
        # Inside the patch there is the path of the method we want to mock.
        # Every time that our code will call the method inside the patch,
        # this will be override by that one we define, as below.
        # Additionally, the patch counts how many times
        # the method inside is called.
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True]
            # This means that the fifth times the error will be rised.
            # At the sixth time it won't rise the error and it will return.
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
