import unittest
import spotipy
from spotify import return_response, gatherNames, gatherDates 


class TestFileName(unittest.TestCase):
    def test_function1(self):
        self.assertEqual((return_response()).status_code, 200)
    
    def test_function2(self):
        json_response = (return_response()).json()
        self.assertIsNotNone(gatherNames)
        
    def test_function3(self):
        json_response = (return_response()).json()
        self.assertIsNotNone(gatherDates)

if __name__ == '__main__':
    unittest.main()
