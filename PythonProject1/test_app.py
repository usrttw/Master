import unittest
from unittest.mock import MagicMock
from intro import Osnova



class TestApp(unittest.TestCase):

    def test_avtorizacia_and_perehod(self):
        osnova_app = Osnova()
        osnova_app.ui.lineEdit.setText("test_user")
        osnova_app.ui.lineEdit_2.setText("test_password")

        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = {'login': 'test_user', 'password': 'test_password'}
        osnova_app.database.cursor = MagicMock(return_value=mock_cursor)

        osnova_app.avtorizacia_and_perehod()

        self.assertNotEqual(osnova_app.ad, None)


if __name__ == '__main__':
    unittest.main()
