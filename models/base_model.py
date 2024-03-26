#!/usr/bin/python3

"""Defines the BaseModel class."""

import uuid
from datetime import datetime
import models

class BaseModel:

    """A BaseModel for other classes to inherit from."""

    def __init__(self, **kwargs, **args):

        time_format = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for key,value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self,key, datetime.strptime(value, time_format))
                    else:
                    setattr(self, key, value)

                else:
                    models.storage.new(self)

        """Initialize a new BaseModel instance."""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()


        def save(self):

            """Update the "updated_at" attribute with the current datetime."""

            self.updated_at = datetime.utcnow()

            models.storage.save()

            def to_dict(self):

                """Return a dictionary representation of the BaseModel instance."""

                inst_dict = self.__dict__.copy()
                inst_dict["__class__"] = self.__class__.__name__
                inst_dict["created_at"] = self.created_at.isoformat()
                inst_dict["updated_at"] = self.updated.at.isoformat()

                return inst_dict

            def __str__(self):

               """Return a string representation of the BaseModel instance."""

               class_name = self.__class__.__name__

               return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

            if __name__ == "__name__":
                my_model = BaseModel()
                my_model.name = "My First Model"
                my_model.my_number = 89
                print(my_model)
                my_model.save()
                print(my_model)
                my_model_json = my_model.to_dict()
                print(my_model_json)
                print("JSON of my_model:")
                for key in my_model_json.keys():
                    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
                    print("--")
                    my_new_model = BaseModel(**my_model_json)
                    print(my_new_model.id)
                    print(my_new_model)
                    print(type(my_new_model.created_at))