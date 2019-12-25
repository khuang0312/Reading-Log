from Book import Book
import unittest

class Test(unittest.TestCase):
    def test_creation_of_new_book(self):
        b = Book()
        self.assertEqual(b.get_title(), "Untitled")
        self.assertEqual(b.get_author(), "Unknown")
        self.assertEqual(b.get_medium(), "Print Book")
        self.assertEqual(b.get_notes(), "")
        self.assertFalse(b.get_completed())
    
    def test_print_big_endian_date(self):
        b = Book()

    
    
if __name__ == '__main__':
    unittest.main()
