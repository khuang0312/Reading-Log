#Kevin Huang
#This module is dedicated to testing the logic of the reading log...

from Book import Book
from datetime import datetime

def addBook(bookList: [Book], title :str="Untitled", author : str="Unknown"):
    bookList.append(Book(title=title, author=author))


def removeBook():
    '''This is slightly confusing how to implement...
        Ask people how this should be interpreted in the case of multiple books being the same...

        Specify the date you want to remove?
        Automatically remove the oldest one?
    '''
    pass

def viewBook(bookList : [Book]) -> str:
    #bookListPrintout = ""
    pass
    
    #return bookListPrintout
        




def main():
    log = []

    
    #username system  #{'default' : []}

    while True:    
        command = input()


        if command in ['q', 'quit']:
            break

        elif command in ['a', 'add']:
            title = input('Title: ')
            author = input('Author: ')
            log.append(Book(title=title, author=author))
        
        elif command in ['r', 'remove']:
            #add functionality to let them take removal back...
            index = int(input('Input Log Number: '))
            del log[index - 1]
        
        elif command in ['c', 'complete']:
            index = int(input('Input Log Number: '))
            log[index - 1].set_completed()

        elif command in ['o', 'output']:
            with open('reading_log.txt', 'w') as reading_log:
                for book in log:
                    if book.get_completed() == False:
                        reading_log.write( book.get_title() + '|' + book.get_author() + '|' + 'Incomplete' + '|' + (book.get_start_date()).isoformat() + '\n')
                    else:
                        reading_log.write(book.get_title() + '|' + book.get_author() + '|' + 'Complete' + '|' + (book.get_start_date()).isoformat() + '|' + (book.get_end_date()).isoformat(), '\n')

        elif command in ['ls', 'load']:
            with open('reading_log.txt', 'r') as reading_log:
                for book in reading_log:
                    book = book.rstrip().split('|')
                    print(book)

                    if book[2] == "Incomplete":
                        b = Book(title=book[0], author=book[1])
                    elif book[2] == "Complete":
                        b = Book(title=book[0], author=book[1], completed=True)
                    
                    b.start_date = datetime.fromisoformat(book[3])
                    
                    if len(book) == 5:
                        b.end_date = datetime.fromisoformat(book[4])
                    
                    log.append(b)

        elif command in ['l', 'log']:
            print()
            print("Reading Log")
            print(90 * '=')
            for counter, book in enumerate(log, 1):
                title = '{:30.30}'.format(book.get_title())
                author = '{:20.20}'.format(book.get_author())
                status = '{:10}'.format('Complete' if book.get_completed() else 'Incomplete')
                print(counter, title + " - " + author + " | Started: " + 
                    book.print_date() + " | " + status)
                
                #d = book.get_start_date().isoformat()
                #print( d)

                #d1 = datetime.fromisoformat(d)
                #print( d1 )
            print(90 * '=')



if __name__ == '__main__':
    main()