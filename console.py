#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from model.engine.file_storage import save
"""console.py model"""


class HBNBCommand(cmd.Cmd):
    """Airbnb_clone program entry point"""

    prompt = "(hbnb) "

    def do_create(self, line):
        """
        Function: create an instance of a class
        Use: create <classname>

        """
        models = ["BaseModel", "User"]
        if line == "BaseModel":
            model = BaseModel()
            model.save()
            print(model.id)
        else:
            print("INVALID")

    def do_show(self, line):
        """
        Function: prints the string representation of an
        instance based on class name and id.
        Use: show <classname.id>

        """

        pass

    def do_all(self, line):
        """
        Function: prints all string representation of all instance
        based on class or all instance when used alone
        Use: all <classname>
             all

        """

        pass

    def do_update(self, line):
        """
        Function: Update an instance based on the class name and id
        by adding or updating attribute and then save the change
        to JSON file.
        Use: update <classname> <id> <attribute_name> <attribute_value>

        """

        pass

    def do_destroy(self, line):
        """
        Function: destroy an instance base on class name and id
        and the save the changes to a JSON file
        Use: destroy <classname.id>

        """

    def do_quit(self, line):
        """
        Quit command to exit the program

        """

        return True

    def do_EOF(self, line):
        """handling end of file imterrupt"""

        return True

    def emptyline(self):
        """updating default emptyline method"""

        HBNBCommand.prompt


if __name__ == "__main__":
    HBNBCommand().cmdloop()
