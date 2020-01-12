#This module contains the command line interface for the reading log...
#Kevin Huang

import argparse

program_description = "This is the command line interface for the reading log"


parser = argparse.ArgumentParser(prog='booklog')
parser.add_argument("add", help="add a book")
parser.add_argument("remove", help="remove a book", type=int)
parser.add_argument("view", help="view list of books")
args = parser.parse_args()
print(args.echo)
print(args.cube**3)