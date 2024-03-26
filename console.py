import cmd
import re
import shlex
import ast
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City

def parse_arguments(arg):
    """Parses the arguments and returns a tuple containing class name, method name, and extra arguments."""
    arg_parts = arg.split('.')
    class_name = arg_parts[0]
    method_with_args = arg_parts[1].split('(')
    method_name = method_with_args[0]
    extra_args = method_with_args[1].split(')')[0] if len(method_with_args) > 1 else ""
    return class_name, method_name, extra_args

def extract_curly_braces_arguments(arg):
    """Extracts arguments enclosed within curly braces."""
    curly_braces = re.search(r"\{(.*?)\}", arg)
    if curly_braces:
        id_with_comma = shlex.split(arg[:curly_braces.span()[0]])
        instance_id = [i.strip(",") for i in id_with_comma][0]
        str_data = curly_braces.group(1)
        try:
            arg_dict = ast.literal_eval("{" + str_data + "}")
        except Exception:
            print("**  invalid dictionary format **")
            return "", ""
        return instance_id, arg_dict
    else:
        commands = arg.split(",")
        if commands:
            try:
                instance_id = commands[0]
            except Exception:
                return "", ""
            try:
                attr_name = commands[1]
            except Exception:
                return instance_id, ""
            try:
                attr_value = commands[2]
            except Exception:
                return instance_id, attr_name
            return instance_id, f"{attr_name} {attr_value}"

class HBNBConsole(cmd.Cmd):
    """
    Console class for interacting with HBNB models.
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "Amenity", "Place", "Review", "State", "City"]

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_EOF(self, arg):
        """
        Handle EOF (Ctrl+D) to exit the program.
        """
        return True

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_create(self, arg):
        """
        Create a new instance of a class and save it to the JSON file.
        Usage: create <class_name>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{commands[0]}()")
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Show the string representation of an instance.
        Usage: show <class_name> <id>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        Usage: destroy <class_name> <id>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Print the string representation of all instances or a specific class.
        Usage: <User>.all()
                <User>.show()
        """
        objects = storage.all()
        commands = shlex.split(arg)
        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))

    def do_count(self, arg):
        
        """Count and retrieve the number of instances of a class."""
        
        objects = storage.all()
        commands = shlex.split(arg)
        if arg:
            class_name = commands[0]
        count = 0
        if commands:
            if class_name in self.valid_classes:
                for obj in objects.values():
                    if obj.__class__.__name__ == class_name:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")

    def do_update(self, arg):
