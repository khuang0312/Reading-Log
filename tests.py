from Book import Book
import unittest

class Test(unittest.TestCase):
    def test_construction_of_new_book(self):
        b = Book()
        self.assertEqual(b.get_title(), "Untitled")
        self.assertEqual(b.get_author(), "Unknown")
        self.assertEqual(b.get_medium(), "Print Book")
        self.assertEqual(b.get_notes(), "")
        self.assertFalse(b.get_completed())

    def test_construction_of_new_book_fails(self):
        self.assertRaises(AssertionError, Book, title=2);
        self.assertRaises(AssertionError, Book, author=2);
        self.assertRaises(AssertionError, Book, medium=2);
        self.assertRaises(AssertionError, Book, completed=2);

    def test_getters_of_new_book(self):
       b = Book(
            title = "Bleach #1 - Strawberry and the Soul Reapers",
            author = "Tite Kubo",
            medium = "comic",
            notes = "Intersting premise.",
            completed = True
            )
        
       self.assertEqual(b.get_title(), "Bleach #1 - Strawberry and the Soul Reapers")
       self.assertEqual(b.get_author(), "Tite Kubo")
       self.assertEqual(b.get_start_date(), b.get_end_date()) 
       self.assertEqual(b.get_medium(), "Comic");
       self.assertTrue(b.get_completed())
               
    def test_print_big_endian_date(self):
        b = Book()
        b.set_date(month=12, day=25, year=2020)
        
        #conventional big endian
        self.assertEqual("2020/12/25", b.print_date(endian='B', year='yyyy', month='mm', day='dd', separator='/', start=True))
        
        #big endian with a weekday
        b.set_date(month=12, day=25, year=2019)
        self.assertEqual("Wed, 2019/12/25", b.print_date(endian='B', year='yyyy', month='mm', day='dd', weekday='ddd', separator='/', start=True))
        self.assertEqual("Wednesday, 2019/12/25", b.print_date(endian='B', year='yyyy', month='mm', day='dd', weekday='dddd', separator='/', start=True))

        #big endian with two digit year
        b.set_date(month=12, day=25, year=2020)
        self.assertEqual("20/12/25", b.print_date(endian='B', year='yy', month='mm', day='dd', separator='/', start=True))
        
        #big endian with three letter month
        self.assertEqual("2020 Dec 25", b.print_date(endian='B', year='yyyy', month='mmm', day='dd', separator=' ', start=True))
        
        #big endian with full month
        self.assertEqual("2020 December 25", b.print_date(endian='B', year='yyyy', month='mmmm', day='dd', separator=' ', start=True))
        
        #big endian with one digit month
        b.set_date(month=9, day=8, year=2020) 
        self.assertEqual("2020/9/08", b.print_date(endian='B', year='yyyy', month='m', day='dd', separator='/', start=True))
        
        #big endian with one digit day
        b.set_date(month=9, day=8, year=2020)
        self.assertEqual("2020/09/8", b.print_date(endian='B', year='yyyy', month='mm', day='d', separator='/', start=True))

    def test_book_completion(self):
        pass

    
    
if __name__ == '__main__':
    unittest.main()
