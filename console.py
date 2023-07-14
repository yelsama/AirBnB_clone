#!/usr/bin/python3
''' console module '''
import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """hbhb entry point"""

    prompt = '(hbnb) '
    classlist = ["BaseModel", "User", "Place", "State", "Amenity", "Review",
                 "City"]

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

    def help_create(self):
        ''' help create '''
        print("Create command to create a new class\n")

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

        all_objs = storage.all()
        for m in all_objs.keys():
            if m == "{}.{}".format(args[0], args[1]):
                print(all_objs[m])
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
            all_objs = storage.all()
            for m in all_objs:
                if m == "{}.{}".format(arg[0], arg[1]):
                    all_objs.pop(m)
                    storage.save()
                    return False
            print('** no instance found **')

    def help_destroy(self):
        ''' help destroy '''
        print("Destroy command to destroy a created object\n")

    def do_all(self, line):
        ''' prints all string representations of instances'''
        arg = line.split()
        all_objs = storage.all()

        if len(arg) == 0:
            for m in all_objs:
                argstr = str(all_objs[m])
                print(argstr)
        elif line not in self.classlist:
            print('** class doesn\'t exist **')
            return False
        else:
            for m in all_objs:
                if m.startswith(arg[0]):
                    argstr = str(all_objs[m])
                    print(argstr)
        return False

    def help_all(self):
        ''' help all'''
        print("All command to show all instances\n")

    def do_update(self,line):
        """updates an instance based on class name and id"""
        arg = line.split()
        flag = 0

        if len(line) == 0:
            print('** class name missing **')
            return False

        try:
            cls = line.split()[0]
            eval("{}()".format(cls))
        except IndexError:
            print('** class doesn\'t exist **')
            return False

        try:
            int_id = line.split()[1]
        except IndexError:
            print('** instance id missing **')
            return False

        all_objs = storage.all()
        try:
            clschange = all_objs["{}.{}".format(cls, int_id)]
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

    def help_update(self):
        '''help update'''
        print("update command to update an attribute\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
