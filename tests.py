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
        self.assertRaises(AssertionError, Book, title=2)
        self.assertRaises(AssertionError, Book, author=2)
        self.assertRaises(AssertionError, Book, medium=2)
        self.assertRaises(AssertionError, Book, completed=2)

    def test_books_with_the_same_title_and_author_are_equal(self):
        b = Book(title = "Oliver Twist",
                 author = "Charles Dickens",
                 medium = "comic"
                 )
        c = Book(title = "Oliver Twist",
                 author = "Charles Dickens",
                 medium = "print"
                 )
        self.assertEqual(b, c)

    def test_books_with_neither_the_same_title_and_author_are_not_equal(self):
        b = Book(title = "Oliver Twist",
                 author = "Charles Dickens"
                 )
        c = Book(title = "Great Expectations",
                 author = "Charles Dickens"
                 )
        self.assertNotEqual(b, c)

        b = Book(title = "Oliver Twist",
                 author = "Charles Dickens"
                 )
        c = Book(title = "Oliver Twist",
                 author = "Jane Austen"
                 )
        self.assertNotEqual(b, c)

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
       self.assertEqual(b.get_medium(), "Comic")
       self.assertTrue(b.get_completed())
               
    def test_print_big_endian_date(self):
        b = Book()
        b.set_date(2019, 12, 25)
        
        #conventional big endian
        self.assertEqual("2019/12/25", b.print_date(endian='B', year='yyyy', month='mm', day='dd', separator='/', start=True))
        
        #big endian with a weekday (weekday goes after...)
        self.assertEqual("2019/12/25, Wed", b.print_date(endian='B', year='yyyy', month='mm', day='dd', weekday='ddd', separator='/', start=True))
        self.assertEqual("2019/12/25, Wednesday", b.print_date(endian='B', year='yyyy', month='mm', day='dd', weekday='dddd', separator='/', start=True))

        #big endian with two digit year
        self.assertEqual("19/12/25", b.print_date(endian='B', year='yy', month='mm', day='dd', separator='/', start=True))
        
        #big endian with three letter month (no commas)
        self.assertEqual("2019 Dec 25", b.print_date(endian='B', year='yyyy', month='mmm', day='dd', separator=' ', start=True))
        
        #big endian with full month (no commas)
        self.assertEqual("2019 December 25", b.print_date(endian='B', year='yyyy', month='mmmm', day='dd', separator=' ', start=True))
        
        #big endian with one digit month
        b.set_date(month=9, day=8, year=2019) 
        self.assertEqual("2019/9/08", b.print_date(endian='B', year='yyyy', month='m', day='dd', separator='/', start=True))
        
        #big endian with one digit day
        b.set_date(month=9, day=8, year=2019)
        self.assertEqual("2019/09/8", b.print_date(endian='B', year='yyyy', month='mm', day='d', separator='/', start=True))
    
    def test_print_little_endian_date(self):
        b = Book()
        b.set_date(2019, 12, 27)
        
        #convention little endian
        self.assertEqual('27/12/2019', b.print_date(endian='L', year='yyyy', month='mm', day='dd', weekday='', separator='/', start=True)) 
        
        #little endian with a weekday (weekday goes before)
        self.assertEqual('Fri, 27/12/2019', b.print_date(endian='L', year='yyyy', month='mm', day='dd', weekday='ddd', separator='/', start=True)) 
        self.assertEqual('Friday, 27/12/2019', b.print_date(endian='L', year='yyyy', month='mm', day='dd', weekday='dddd', separator='/', start=True)) 
        
        #little endian with two digit year
        self.assertEqual('27/12/19', b.print_date(endian='L', year='yy', month='mm', day='dd', weekday='', separator='/', start=True))

        #little endian with a three letter month
        self.assertEqual("27 Dec 2019", b.print_date(endian='L', year='yyyy', month='mmm', day='dd', separator=' ', start=True))

        #little endian with full month
        self.assertEqual("27 December 2019", b.print_date(endian='L', year='yyyy', month='mmmm', day='dd', separator=' ', start=True))

        #little endian with one digit month
        b.set_date(2019, 9, 8)
        self.assertEqual("08/9/2019", b.print_date(endian='L', year='yyyy', month='m', day='dd', separator='/', start=True))
        
        #little endian with one digit day
        self.assertEqual("8/09/2019", b.print_date(endian='L', year='yyyy', month='mm', day='d', separator='/', start=True))
    
    def test_print_middle_endian_date(self):
        b = Book()
        b.set_date(month=12, day=27, year=2019)
        
        #convention middle endian
        self.assertEqual('12/27/2019', b.print_date(endian='M', year='yyyy', month='mm', day='dd', weekday='', separator='/', start=True)) 
        
        #little middle with a weekday (weekday goes before)
        self.assertEqual('Fri, 12/27/2019', b.print_date(endian='M', year='yyyy', month='mm', day='dd', weekday='ddd', separator='/', start=True)) 
        self.assertEqual('Friday, 12/27/2019', b.print_date(endian='M', year='yyyy', month='mm', day='dd', weekday='dddd', separator='/', start=True)) 
        
        #middle endian with two digit year
        self.assertEqual('12/27/19', b.print_date(endian='M', year='yy', month='mm', day='dd', weekday='', separator='/', start=True))

        #middle endian with a three letter month (with comma in middle)
        self.assertEqual("Dec 27, 2019", b.print_date(endian='M', year='yyyy', month='mmm', day='dd', separator=' ', start=True))

        #middle endian with full month (with comma in middle)
        self.assertEqual("December 27, 2019", b.print_date(endian='M', year='yyyy', month='mmmm', day='dd', separator=' ', start=True))

        #middle endian with one digit month
        b.set_date(month=9, day=8, year=2019)
        self.assertEqual("9/08/2019", b.print_date(endian='M', year='yyyy', month='m', day='dd', separator='/', start=True))
        
        #middle endian with one digit day
        self.assertEqual("09/8/2019", b.print_date(endian='M', year='yyyy', month='mm', day='d', separator='/', start=True))

    def test_print_time(self):
        b = Book()
        b.set_date(month=12, day=27, year=2019, hour=1, minute=18, second=56)
        self.assertEqual("01:18 PST", b.print_timestamp(hour_truncated=False, seconds=False, military=True, utc=False, separator=':', start=True))
        self.assertEqual("1:18 PST", b.print_timestamp(hour_truncated=True, seconds=False, military=True, utc=False, separator=':', start=True))
        self.assertEqual("01:18:56 PST", b.print_timestamp(hour_truncated=False, seconds=True, military=True, utc=False, separator=':', start=True))
        
        b.set_date(month=12, day=27, year=2019, hour=13, minute=18, second=56)
        self.assertEqual("13:18 PST", b.print_timestamp(hour_truncated=False, seconds=False, military=True, utc=False, separator=':', start=True))
        self.assertEqual("01:18 PM PST", b.print_timestamp(hour_truncated=False, seconds=False, military=False, utc=False, separator=':', start=True))
        self.assertEqual("21:18 UTC", b.print_timestamp(hour_truncated=False, seconds=False, military=True, utc=True, separator=':', start=True))

    def test_book_completion(self):
        pass

    
    
if __name__ == '__main__':
    unittest.main()
