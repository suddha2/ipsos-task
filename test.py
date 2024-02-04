import unittest
from service import ipsos

class TestService(unittest.TestCase):

    def setUp(self):
        self.ipsosSrv = ipsos.IpsosService()

    def test_find_code (self):
        data = self.ipsosSrv.find_code(5001)
        self.assertEqual(len(data),1,"Match found")
    
    def test_find_id (self):
        data = self.ipsosSrv.find_id("thanks")
        self.assertEqual(len(data),2,"2 Matches found")

if __name__ == '__main__':
    unittest.main()