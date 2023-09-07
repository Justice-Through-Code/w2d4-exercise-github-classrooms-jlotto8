import io
import unittest
from unittest.mock import patch
from jtc_technical_pq import jtc_technical

class TestJtcTechnical(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_jtc_technical_pq(self, mock_stdout):
        # Call the jtc_technical function, which will print to stdout
        jtc_technical()
        
        # Assert that the printed output matches the expected output
        self.assertEqual('Hello World?\n', mock_stdout.getvalue())

    def test_step_3_is_commented(self):
        # Open the jtc_technical_pq.py file
        with open('jtc_technical_pq.py', 'r') as file:
            code = file.read()
        
        # Check if Line 6 (the call to jtc_technical) is commented out
        self.assertTrue('#jtc_technical()' in code)

if __name__ == "__main__":
    unittest.main()
