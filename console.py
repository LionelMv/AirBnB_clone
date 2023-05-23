#!/usr/bin/python3
"""contains the entry point of the command intepreter"""


import cmd
from models.base_model import BaseModel


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
        elif line not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        else:
            obj = eval(line)
            obj.save()
            print(obj.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
