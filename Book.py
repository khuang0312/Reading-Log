#This module contains the Book class which describes each book in a user's reading list.
#Kevin Huang

#importing the datetime class
from time import strftime
from datetime import datetime
from dateutil import tz


#in progress
#check set_date (What's up with fold argument? Does it actually convert a local time to its UTC time?)
#print_date
#get_time_read

#prepare to reimplement this program with the datetime and calendar libaries which are far more reliable....
#prevent the 2038 issue!!!

class Book:
    #DATE_FORMAT is a static variable made to help format the date that a book is read

    YEAR_FORMAT = {
        'yy' : '%y',
        'yyyy' : '%Y'
    }

    MONTH_FORMAT = {
        'm' : '%m',
        'mm' : '%m',
        'mmm' : '%b',
        'mmmm' : '%B'
    }

    DAY_FORMAT = {
        'd':  '%d',
        'dd': '%d'
    }

    WEEKDAY_FORMAT = {
        'ddd' : '%a',
        'dddd': '%A',
        '' : ''
    }
    
    ENDIAN_FORMAT = ['B', 'L', 'M']

    SEPARATOR_FORMAT = ['/', '.', '-', ' ']
        
    
    #MEDIUM is a static variable to help set the medium...
    MEDIUM = {
        "picture"    : "Picture Book",
        "print"      : "Print Book",
        "comic"      : "Comic",
        "audio"      : "Audio Book",
        "fanfiction" : "Fanfiction"
        }

    TIME_UNIT = {
        '24h'     : '%H',    # 24 hour
        '12h'     : '%I',    # 12 hour
        'mm'      : '%M',    # minutes
        'ss'      : '%S',    # seconds
        'AMPM'    : '%p',    # AM or PM
        'tz'      : '%Z'     # Time zone name
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

        #we initialize the start date with the current date in UTC format
        self.start_date = datetime.now(tz.UTC) 
        
        # if a new book is "completed"
        if completed: 
            self.end_date = self.start_date
        
        # if a new book is "not completed"
        else:
            self.end_date = None

        self.medium = medium
        self.notes = notes
        self.completed = completed

    def __repr__(self) -> str:
        '''Returns a string that creates the same Book object when evaluated'''
        return f'Book({self.title}, {self.author})'

    def __str__(self) -> str:
        '''Returns a string representing a Book'''
        return f'{self.title}, {self.author}'

    def __eq__(self, other):
        '''A Book object is the same as another if they both have the same author and title.'''
        return isinstance(other, Book) and self.title == other.title and self.author == other.author

    def __ne__(self, other):
        '''A Book object is not equal to anything other than another Book object with the same author and title''' 
        return not self.__eq__(other)

    def set_title(self, new_title : str):
        '''Sets a book's title to the new one'''
        assert isinstance(new_title, str) and new_title != "", "Argument must be a non-empty string."
        self.title = new_title

    def set_author(self, new_author : str):
        '''Sets a book's author to the new one'''
        assert isinstance(new_author, str) and new_author != "", "Argument must be a non-empty string."
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

    def set_completed(self):
        '''Sets a book's completion status to True and sets the end time to the time when this method is called'''
        self.completed = True
        self.end_date = datetime.now(tz.UTC) 
    
    def set_incompleted(self):
        '''Sets a book's completion status to False and resets the end time back to None'''
        self.completed = False
        self.end_date = None
    
    def set_date(self, year : int, month : int, day : int, hour : int=0, minute : int=0, second : int=0, start : bool=True):
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

        try:
            #creating a datetime object in local time
            date = datetime(year, month, day, hour, minute, second, microsecond=0, tzinfo=tz.gettz(), fold=0)

        except ValueError:
            print("Arguments are of an invalid type or are invalid values...")
        
        else:
            #convert custom date to UTC...
            utc_date = date.astimezone(tz=tz.UTC)

            #present_date is the current time in UTC...
            present_date = datetime.now(tz.UTC) 
            
            #if we're replacing the start date
            if start == True:
                #if there's no end date, the start date should be at latest today's date...
                if self.end_date == None:
                    if utc_date < present_date:
                        self.start_date = utc_date

                #if there's an end date, the start date just has to be earlier than the end_date...
                elif utc_date < self.end_date:
                    self.start_date = utc_date
            
            #if we're replacing the end date... the end date should be later than start_date
            elif start == False and utc_date > self.start_date:
                self.end_date = utc_date

   
    def print_date(self, endian : str='M', year : str='yyyy', month : str='mm', day : str='dd', weekday : str='', separator : str='/', start : bool=True) -> str:
        '''Returns a string representation of the date
        
        Keyword arugments:
        
        endian:
        'B' – big-endian (year, month, day), e.g. 2006-04-22 or 2006.04.22 or 2006/04/22 or 2006 April 22
        'L' – little-endian (day, month, year), e.g. 22.04.2006 or 22/4/2006 or 22-04-2006 or 22 April 2006
        'M' – middle-endian (month, day, year), e.g. 04/22/2006 or April 22, 2006
        
        year:
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

        weekday:
        ''    -- nothing happens.
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
        
        assert endian in Book.ENDIAN_FORMAT, 'Argument \'endian\' must be either \'B\', \'M\', or \'L\'. '
        assert year in Book.YEAR_FORMAT, 'Argument \'year\' must be either \'yy\' or \'yyyy\'.'
        assert month in Book.MONTH_FORMAT, 'Argument \'month\' must be either \'mmmm\', \'mmm\', \'mm\', or \'m\'.'
        assert day in Book.DAY_FORMAT, 'Argument \'day\' must either be \'d\' or \'dd\'.'
        assert weekday in Book.WEEKDAY_FORMAT, 'Argument \'weekday\' must either be \'\', \'ddd\' or \'dddd\''
        assert separator in Book.SEPARATOR_FORMAT, 'Argument \'seperator\' must either be \'/\', \'.\', \'-\', or \' \'.'

        year_format = Book.YEAR_FORMAT[year]
        month_format = Book.MONTH_FORMAT[month]
        day_format = Book.DAY_FORMAT[day]
        weekday_format = Book.WEEKDAY_FORMAT[weekday]

        if start == True:
            year_string = self.start_date.strftime(year_format)
            month_string = self.start_date.strftime(month_format)
            day_string = self.start_date.strftime(day_format)   #we want the day number in all cases... 
            weekday_string = self.start_date.strftime(weekday_format) if weekday_format != '' else ''
        
        #if the start_date is False, it still doesn't matter if the end_date isn't there
        elif self.end_date != None:
            year_string = self.end_date.strftime(year_format)
            month_string = self.end_date.strftime(month_format)
            day_string = self.end_date.strftime(day_format)
            weekday_string = self.end_date.strftime(weekday_format)  if weekday_format != '' else '' 

        #to change the length of the day or month to 1
        if month == 'm':
            month_string = month_string[-1] if int(month_string) < 10 else month_string
        if day == 'd':
            day_string = day_string[-1] if int(day_string) < 10 else day_string
        
        #order it based on endian
        if endian == 'B':
            #modify the date_string based on the seperator...
            date_string = year_string + separator + month_string + separator + day_string
            if weekday != '':
                date_string += ', ' + weekday_string

        elif endian == 'L':
            date_string =  day_string + separator + month_string + separator + year_string
            if weekday != '':
                date_string = weekday_string + ', ' + date_string
        
        elif endian == 'M':
            date_string =  month_string + separator + day_string + ',' + separator + year_string  if month in ['mmmm', 'mmm'] else\
                month_string + separator + day_string + separator + year_string
                
            if weekday != '':
                date_string = weekday_string + ', ' + date_string
 
        return date_string
    
    def print_timestamp(self, hour_truncated : bool=False, seconds : bool=False, military : bool=True, utc : bool=False, separator : str=':', start=True) -> str:
        '''returns the timestamp in a string
        
           seconds - will show seconds if True; otherwise not
           military - will show time in 24 hour format if True; otherwise 12 hours
           utc - will show time in UTC format if True; otherwise it will use local time zone
        
           If the time is 1:00:13AM, Pacific Standard Time
           
           Default:
           01:00 PST

           Hour_truncates = True
           1:00:13 PST

           Seconds = True
           01:00:13 PST

           Military = False
           01:00 AM PST

           UTC = True
           09:00 AM UTC
           
            '24h'     : '%H',    # 24 hour
            '12h'     : '%I',    # 12 hour
            'mm'      : '%M',    # minutes
            'ss'      : '%S',    # seconds
            'AMPM'    : '%p',    # AM or PM
            'tz'      : '%z'     # Time zone name
        
        '''
        #deciding to give the start time or the end time...
        if start == True:
            date = self.start_date
          
        elif start == False:
            date = self.end_date

        #changes the timezone to local time if utc is False
        if utc == False:
            date = date.astimezone(tz=tz.tzlocal())
        
        #changing between 24 and 12 hour time and determining the AM or PM
        if military == True:
            hour_string = date.strftime(Book.TIME_UNIT['24h'])
            ampm_string = ''
        elif military == False:
            hour_string = date.strftime(Book.TIME_UNIT['12h'])
            ampm_string = ' ' + date.strftime(Book.TIME_UNIT['AMPM'])

        minute_string = date.strftime(Book.TIME_UNIT['mm'])
        second_string = separator + date.strftime(Book.TIME_UNIT['ss']) if seconds else ''

        #truncating hours
        if hour_truncated == True and int(hour_string) < 10:
            hour_string = hour_string[1]
        
        #preparing the time zone name
        tz_string = ' ' + date.strftime(Book.TIME_UNIT['tz'])

        return hour_string + separator + minute_string + second_string + ampm_string + tz_string       
            
    
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

    def get_completed(self) -> bool:
        '''returns whether the book has been completed'''
        return self.completed

    def get_start_date(self) -> datetime:
        '''returns when the user started reading the book'''
        return self.start_date

    def get_end_date(self) -> datetime:
        '''returns when the user has finished the book'''
        return self.end_date if self.completed else None 

    def get_time_read(self, unit: str='seconds') -> int:
        '''returns time spent reading the book in a given unit

            this doesn't give the true amount of months, weeks, years...
            in the time span, mainly an approximation that should suffice...

            arguments supported:
            seconds
            minutes
            hours
            days
            weeks
            months
            years         
        '''

        if self.end_date == None:
            time_span = datetime.now(tz.UTC) - self.start_date
        else:
            time_span = self.end_date - self.start_date

        if unit == "seconds":
            return time_span.seconds
        
        elif unit == "hours":
            return time_span.seconds // 60
        
        elif unit == "hours":
            return time_span.seconds // 360

        elif unit == "days":
            return time_span.days

        elif unit == "weeks":
            return time_span.days // 7

        elif unit == "months":
            return time_span.days // 30

        elif unit == "years":
            return time_span.days // 365
