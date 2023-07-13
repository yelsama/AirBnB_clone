#!/usr/bin/python3
''' console module '''
import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json

class HBNBCommand(cmd.Cmd):
    """hbhb entry point"""

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """end of file"""
        return True

    def do_quit(self, arg):
        """quit program"""
        return True

    def help_quit(self):
        """help quit"""
        print("Quit command to exit program\n")

    def emptyline(self):
        """emptyline + enter shouldnt execute"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
