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
            args = line.split()
            objdict = storage.all()
            if args[0] not in HBNBCommand.__valid_classes:
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
            args = line.split()
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

    def do_all(self, line):
        """Prints string representation of all instances.
        """
        # do_all(BaseModel)
        if line != "":
            args = line.split()
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for key, obj in storage.all().items()
                      # if __class__.__name__ == args[0]
                      if type(obj).__name__ == args[0]]
                      # if obj.__class__.__name__ == args[0]
                print(nl)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_update(self, line):
        """Update if given exact object, exact attribute"""
        objdict = storage.all()
        args = line.split()
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[3]))
            # setattr(objdict[key], args[2], cast(arg3))
            objdict[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
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
