import json
import os
from models.base_model import BaseModel

class FileStorage:

    """Class for serializing and deserializing instances to and from JSON."""

    __file_path = "file.json"
    __objects = {}

    def new(self, obj):

        """Adds a new object to the storage dictionary."""

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

        def all(self):

            """Returns the dictionary __objects."""

            return FileStorage.__objects

        def save(self):
            
            """Serializes __objects to JSON and saves it to file."""

        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)
            
            def reload(self):
                
                """Deserializes the JSON file to __objects."""

                if os.path.isfile(FileStorage.__file_path):
                    with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                        try:
                            obj_dict = json.load(file)
                            for key, value in obj_dict.items():
                                class_name, obj_id = key.split(".")
                                cls = eval(class_name)
                                instance = cls(**value)
                                FileStorage.__objects[key] = instance

                        except Exception:
                            pass