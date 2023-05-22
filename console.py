#!/usr/bin/python3
"""contains the entry point of the command intepreter"""


import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """class definition"""
    prompt = "(hbnb)"
    __valid_classes = ['BaseModel']

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
        elif line not in HBNBCommand.__valid_classes:
            print("** class doesn't exist **")
        else:
            obj = eval(line)()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(' ')
            objdict = storage.all()
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = f"{args[0]}.{args[1]}"
                if key not in objdict:
                    print("** no instance found **")
                else:
                    print(objdict[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(' ')
            objdict = storage.all()
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = f"{args[0]}.{args[1]}"
                if key not in objdict:
                    print("** no instance found **")
                else:
                    del objdict[key]
                    storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
