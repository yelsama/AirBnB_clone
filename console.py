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
    classlist = ["BaseModel"]

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

    def do_create(self, classname):
        """create a new instance"""
        if len(classname) == 0:
            print('** class name missing **')
        elif classname not in self.classlist:
            print('** class doesn\'t exist **')
            return False
        else:
            new = eval("{}()".format(classname))
            new.save()
            print(new.id)

    def do_show(self, line):
        """prints the string representation of an instance"""
        arg = line.split()
        if len(arg) == 0:
            print('** class name missing **')
            return False
        elif arg[0] not in self.classlist:
            print('** class doesn\'t exist **')
            return False

        if len(arg) < 2:
            print('** instance id missing **')
            return False

        objlist = storage.all()
        for m in objlist.keys():
            if m == "{}.{}".format(args[0], args[1]):
                print(objlist[m])
                return False
        print('** no instance found **')

    def help_show(self):
        ''' help show '''
        print("Show command to display the string representation of class\n")

    def do_destroy(self, line):
        """deletes an instance"""
        arg = line.split()
        if len(line) == 0:
            print('** class name missing **')
            return False
        elif arg[0] not in self.classlist:
            print('** class doesn\'t exist **')
            return False
        elif len(arg) < 2:
            print('** instance id missing **')
            return False
        else:
            objlist = storage.all()
            for m in objlist:
                if m == "{}.{}".format(arg[0], arg[1]):
                    objlist.pop(m)
                    storage.save()
                    return False
            print('** no instance found **')

    def do_all(self, line):
        ''' prints all string representations of instances'''
        arg = line.split()
        objlist = storage.all()

        if len(arg) == 0:
            for m in objlist:
                argstr = str(objlist[m])
                print(argstr)
        elif line not in self.classlist:
            print('** class doesn\'t exist **')
            return False
        else:
            for m in objlist:
                if m.startswith(arg[0]):
                    argstr = str(objlist[m])
                    print(argstr)
        return False

    def do_update(self,line):
        """updates an instance based on class name and id"""
        arg = line.split()
        flag = 0

        if len(line) == 0:
            print('** class name missing **')
            return False

        try:
            cls = line.split()[0]
            eval("{}{}".format(cls))
        except IndexError:
            print('** class doesn\'t exist **')
            return False

        try:
            int_id = line.split()[1]
        except IndexError:
            print('** instance id missing **')
            return False

        objlist = storage.all()
        try:
            clschange = objlist["{}.{}".format(cls, int_id)]
        except IndexError:
            print('** no instance found **')
            return False

        try:
            attri = line.split()[2]
        except IndexError:
            print('** attribute name missing **')
            return False

        try:
            attrivalue = line.split()[3]
        except IndexError:
            print('** value missing **')
            return False

        if attrivalue.isdecimal() is True:
            setattr(clschange, attri, int(attrivalue))
            storage.save()
        else:
            try:
                setattr(clschange, attri, float(attrivalue))
                storage.save()
            except:
                setattr(clschange, attri, str(attrivalue))
                storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
