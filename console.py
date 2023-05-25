#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class definition"""
    prompt = "(hbnb)"
    valid_classes = ["BaseModel", "User", "State", "City",
                     "Amenity", "Place", "Review"]

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """do nothing"""
        pass

    def do_create(self, line):
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        else:
            # e.g. obj = BaseModel()
            obj = eval(line)()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = f"{args[0]}.{args[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = f"{args[0]}.{args[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Prints string representation of all instances.
        """
        new_list = []
        if line != "":
            if line not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
            else:
                new_list = [str(obj) for obj in storage.all().values()
                            if type(obj).__name__ == line]
                # if __class__.__name__ == args[0]
                # if obj.__class__.__name__ == args[0]
                # new_list = [str(obj) for k, obj in storage.all().items()
                # if k.split(".")[0] == line[0]]
                print(new_list)
        else:
            new_list = [str(obj) for obj in storage.all().values()]
            print(new_list)

    def do_update(self, line):
        """Update if given exact object, exact attribute"""
        args = line.split()
        if len(args) >= 4:
            key = f"{args[0]}.{args[1]}"
            # Finding attribute type (casted).
            arg_type = type(eval(args[3]))
            arg3 = args[3].strip('"')
            arg3 = arg3.strip("'")
            setattr(storage.all()[key], args[2], arg_type(arg3))
            storage.all()[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
