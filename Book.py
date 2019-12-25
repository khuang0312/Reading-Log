#This module contains the Book class which describes each book in a user's
#   reading list.

from time import gmtime, strptime, strftime


class Book:
    #DATE_FORMAT is a static variable made to help format the date that a book is read

    DATE_FORMAT = {
        #year specifier
        'y' : '%y',
        'yyyy' : '%Y',
        
        #month specifiers
        'm' : '%m',
        'mm' : '%m',
        'mmm' : '%b',
        'mmmm' : '%B',
        
        #day specifiers
        'd' : '%d',
        'dd' : '%d',

        #endian specifier
        'B' : None,
        'L' : None,
        'M' : None,
        
        #seperator specifier
        '/' : None,
        '.' : None,
        '-' : None,
        ' ' : None 
        }
    
    #MEDIUM is a static variable to help set the medium...
    MEDIUM = {
        "picture" : "Picture Book",
        "print"   : "Print Book",
        "comic"   : "Comic",
        "audio"   : "Audio Book"
        }

    def __init__(self, title : str="Untitled", author : str="Unknown", medium : str="print", notes : str="", completed : bool=False):
        '''Constructs a book with the following parameters
        
        Keyword arguments:
        title     -- the title of the book 
        author    -- the author of the book
        medium    -- the medium of the book: audio book, picture book, comic book, audio book
        notes     -- any comments a reader might have
        completed -- indicates the completion status of a book
        
        Other Attributes
        start_date -- the date that one started reading...
        end_date   -- the date that one finished reading
        '''
        assert isinstance(title, str), "Book.__init__ : argument \'title\' must be a string."
        assert isinstance(author, str), "Book.__init__ : argument \'author\' must be a string."
        assert isinstance(medium, str), "Book.__init__ : argument \'medium\' must be a string."
        assert isinstance(notes, str), "Book.__init__ : argument \'notes\' must be a string."
        assert isinstance(completed, bool), "Book.__init__ : argument \'completed\' must be a bool."
        
        self.title = title
        self.author = author
        self.start_date = gmtime()
        self.end_date = self.start_date
        self.medium = medium
        self.notes = notes
        self.completed = completed

    def __repr__(self) -> str:
        '''Returns a string that creates the same Book object when evaluated'''
        return f'Book({self.title}, {self.author}, {self.start_date}, {self.end_date}, {self.medium}, {self.completed}, {self.notes})'

    def set_title(self, new_title : str):
        '''Sets a book's title to the new one'''
        assert isinstance(new_title, str), "Argument must be a string."
        self.title = new_title

    def set_author(self, new_author : str):
        '''Sets a book's author to the new one'''
        assert isinstance(new_author, str), "Argument must be a string."
        self.author = new_author

    def set_medium(self, new_medium : str):
        '''Sets a book's medium to the new one'''
        assert new_medium in Book.MEDIUM, "Argument must be either \'picture\', \'print\', \'comic\', or \'audio\'."
        self.medium = new_medium

    def set_notes(self, notes : str):
        '''Sets book's notes to the new one
            
           Notes are only 1000 characters long to prevent the logs from getting too big.
        '''
        assert isinstance(notes, str) and len(notes) <= 1000, "Argument must be a string of 1000 or less characters."
        self.notes = notes

    def set_completed(self, completed : bool):
        '''Sets a book's completion status
            
           If we want to mark a book as finished, the end_date is initialized to the date that this method is executed.
           If we want to mark a book as incomplete, we reinitialize the end_date to the start_date.
        '''
        assert isinstance(completed, bool), "Argument must be a bool."
        
        if completed == True:
            self.end_date = gmtime()
        else:
            self.end_date = start_date()

        self.completed = completed
    
    def set_date(self, month : int, day : int, year : int, hour : int=0, minute: int=0, second: int=0, start : bool=True):
        '''Sets either a book's start date or end date to a new one.
            
           If start is True, this will change the starting date. Otherwise, the ending date.
           
           Month   [0-12]
           Day     [0-31]
           Hour    [0,24]
           Minutes [0,59]
           Second  [0,59]

           By default, you will only need the month, day, and year. That will mean that the time will be set to midnight of that day.
           
           e.g.
           January 1st, 2020, 12:00:00AM
           January 1st, 2020, 00:00:00
        '''
        date = str(hour) + ':' + str(minute) + ':' + str(second) + ', ' + str(month) + ' ' + str(day) + ', ' + str(year)
        
        if start == True:
            self.start_date = strptime(date, "%h:%M:%S, %b %d, %Y")
        else:
            self.end_date = strptime(date, "%h:%M:%S, %b %d, %Y")
   
    def print_date(self, endian='M', year='yyyy', month='mm', day='dd', separator='/', start=True) -> str:
        '''Returns a string representation of the date
        
        Keyword arugments:
        
        endian:
        'B' – big-endian (year, month, day), e.g. 2006-04-22 or 2006.04.22 or 2006/04/22 or 2006 April 22
        'L' – little-endian (day, month, year), e.g. 22.04.2006 or 22/4/2006 or 22-04-2006 or 22 April 2006
        'M' – middle-endian (month, day, year), e.g. 04/22/2006 or April 22, 2006
        
sertEqual() are summarized in the following table. Note that it’s usually not necessary to invoke these me        year:
        'yy' – two-digit year, e.g. 06
        'yyyy' – four-digit year, e.g. 2006
        
        month:
        'm' – one-digit month for months below 10, e.g. 4
        'mm' – two-digit month, e.g. 04
        'mmm' – three-letter abbreviation for month, e.g. Apr
        'mmmm' – month spelled out in full, e.g. April
        
        day:
        'd' – one-digit day of the month for days below 10, e.g. 2
        'dd' – two-digit day of the month, e.g. 02
        'ddd' – three-letter abbreviation for day of the week, e.g. Tue
        'dddd' – day of the week spelled out in full, e.g. Tuesday
        
        Separators of the components:
        "/" – stroke (slash)
        "." – dots or full stops/points (periods)
        "-" – hyphens or dashes
        " " – spaces

        start:
        True - start date of the book
        False - end date of the book
        '''
        assert endian in Book.DATE_FORMAT, 'Argument \'endian\' must be either \'B\', \'M\', or \'L\'. '
        assert year in Book.DATE_FORMAT, 'Argument \'year\' must be either \'yy\' or \'yyyy\'.'
        assert month in Book.DATE_FORMAT, 'Argument \'month\' must be either \'mmmm\', \'mmm\', \'mm\', or \'m\'.'
        assert day in Book.DATE_FORMAT, 'Argument \'day\' must either be \'d\' or \'dd\'.'
        assert separator in Book.DATE_FORMAT, 'Argument \'seperator\' must either be \'/\', \'.\', \'-\', or \' \'.'

        year_format = Book.DATE_FORMAT[year]
        month_format = Book.DATE_FORMAT[month]
        day_format = Book.DATE_FORMAT[day]
        
        if endian == 'B':
            date_format = year_format + separator + month_format + separator + day_format

        elif endian == 'L':
            date_format = day_format + separator +  month_format + separator + year_format

        elif endian == 'M':
            date_format = month_format + separator + day_format + separator + year_format
        
        
        return strftime(date_format, self.start_date) if start == True else strftime(date_format, self.end_date)
    
    def get_title(self) -> str:
        '''returns the title of the book'''
        return self.title

    def get_author(self) -> str:
        '''returns the name of the author'''
        return self.author

    def get_medium(self) -> str:
        '''returns the medium of the book in a neater format'''
        return Book.MEDIUM[self.medium]

    def get_notes(self) -> str:
        '''returns the notes associated with a book'''
        return self.notes

    def get_completed(self) -> str:
        '''returns whether the book has been completed'''
        return self.completed

    def get_start_date(self) -> str:
        '''returns when the user started reading the book'''
        return self.start_date

    def get_end_date(self) -> str:
        '''returns when the user has finished the book'''
        return self.end_date
